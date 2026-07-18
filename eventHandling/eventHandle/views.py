# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from eventHandle.models import EventRegister, UserRegister, EventHandle
# from authApp.models import User
from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
# Create your views here.


@csrf_exempt
@login_required
def user_register(request):
    # User Registeration before Event Placing;
    try:
        if request.method == 'POST':
            if request.user.is_authenticated:
                loggedUser = request.user
                setData = json.loads(request.body)
                firstName = setData.get('First Name')
                lastName = setData.get('Last Name')
                address = setData.get('Address')
                phoneNumber = setData.get('Phone Number')
                
                UserRegister.objects.create(firstName=firstName,user=loggedUser, lastName=lastName, address=address, phoneNumber=phoneNumber)
                return JsonResponse({
                    'status' : 'The User is Authenticated and is fetched:',
                    'message': loggedUser.username,
                    'First Name': firstName,
                    'Last Name': lastName,
                    'Address': address,
                    'Contact Number': phoneNumber
                })
            else: 
                return JsonResponse({
                    'message': 'No User Found:'
                })
    except json.JSONDecodeError as error:
        return JsonResponse({
            'Status': 'Exception Caught',
            'Message': str(error)
        })
    return JsonResponse({
        'status': 'Successfull',
        'message': "Working Correctly"
    })

@csrf_exempt
@login_required
def event_registeration(request):
    # Events Registeration
    try:
        if request.method == 'POST':
            setEventData = json.loads(request.body) # Getting data fetched as requested.
            titleName = setEventData.get('Event Name')
            eventPlace = setEventData.get('Place Name')
            eventScheduled = setEventData.get('Event Date')
            eventTime = datetime.strptime(eventScheduled, "%Y-%m-%d %H:%M:%S")
            capacity = setEventData.get('Event Capacity')
            totalCapacity = setEventData.get('Total Capacity')
            registeredEvent = EventRegister.objects.create(title=titleName, place=eventPlace, date=eventTime, capacity=capacity, totalCapacity=totalCapacity)
            
            registeredEvent.save()
            return JsonResponse({
                'status': "Successfully Created the Event:",
                'EventTitle': titleName,
                'Event Place': eventPlace,
                'Event Date': eventTime,
                'Seating Capacity': capacity,
                'Total Capacity': totalCapacity
                })
    except json.JSONDecodeError as error: 
        return JsonResponse({
            'Status': "Exception Caught",
            'Message': str(error)
        })
    return JsonResponse({
        'status': 'Passed',
        'message': "Event Registeration URL is working completely:"
    })

@csrf_exempt
@login_required
def event_list(request):
    # All The Events are listed.
    setData = EventRegister.objects.values('title', 'place', 'date', 'capacity', 'totalCapacity')
    getData = list(setData)
    event_list = [] # Appending the Data that is extracted from the getData
    for item in getData:
        event_list.append({'Name': item['title'], 'Place':item['place'], 'Date':item['date'], 'Capacity':item['capacity'], 'Total Capacity':item['totalCapacity']})
    return JsonResponse({
        'status': 'Passed',
        'Data': event_list
    })

@csrf_exempt
@login_required
def user_list(request):
    # All the users fetched.
    setUserData = UserRegister.objects.filter() # Getting all the data filtered and passed to the said variable
    # print(setUserData) Debugging...
    user_data = [] # Appending the Fetched data.
    for item in setUserData:
        print(item.user.email)
        user_data.append({
            'First Name': item.firstName, 'Last Name': item.lastName, 'User Name':item.user.username, 'Email':item.user.email, 'Address':item.address, 'Contact Number': item.phoneNumber
        })
    # print(f'Data is fetched and is appended: ---> {user_data}') Optional to check and debug...
    return JsonResponse({
        'Status': 'Data Fetched',
        'Data': user_data
    })

@csrf_exempt
@login_required
def event_handle(request):
    # Event Handling:
    try:
        if request.method == 'POST':
            setData = json.loads(request.body) # Data to be Loaded and Extracted.
            userData = UserRegister.objects.get(user=request.user) # Extracting the Existing User.
            try:
                eventID = setData.get('RegisteredId') # Letting the user puts the Id he wants to registered.
            except ValueError as error:
                return JsonResponse({
                    'status': f'(Error: Exception Caught---> {str(error)})'
                })
            try:
                eventData = EventRegister.objects.get(id=eventID) # Extracting the Data against the given ID..
            except EventRegister.DoesNotExist as error:
                return JsonResponse({
                    'Status': f'Error: Exception Caught ---> No Event Found: {str(error)}'
                })
            seatingCapacity = setData.get('Reserved Seats')
            leftSeats = 0
            if ((seatingCapacity <= eventData.capacity)): # It must ensures that the seating Capacity must be less then the registered Seats of the Event
                leftSeats = eventData.capacity - seatingCapacity # Finally getting the seats subtracted.
            else: 
                return JsonResponse({
                    'Message': 'The Capacity must be lesser than the allowed Capacity'
                })
            eventData.capacity = leftSeats # Updating the Seats of EventRegister Model
            eventData.save();
            EventHandle.objects.create(registeredUser=userData, userTicket=eventData, seatingCapacity=seatingCapacity)
            return JsonResponse({
                'status': eventData.title
            })
            # print(f'Event Data Fetched: {eventData}')
    except json.JSONDecodeError as error:
        return JsonResponse({
            'Status': 'Failed',
            'Message': f'Error: Exception Caught in json:{str(error)}'
        })
    return JsonResponse({
        'status': 'Passed',
        'message': "Event Handling URL is working completely:"
    })
    

@csrf_exempt
@login_required
def regiseteredEvent_list(request):
    if request.method == 'POST':
        user_data = UserRegister.objects.get(user=request.user)
        setEventData = EventHandle.objects.filter(registeredUser = user_data)
        # print(f'Events are fetched: {setEventData}')
        item_added = [] # Appending all the data to new List for getting it extracted to the Json Response:
        for items in setEventData:
            item_added.append({
                "Title": items.userTicket.title,
                "User": items.registeredUser.user.username,
                'Reserved Seats': items.seatingCapacity
            })
            
        return JsonResponse({
            'Message': item_added
        })
    return JsonResponse({
        'Status': "Passed"
    })

@csrf_exempt
@login_required
def cancelEvent(request):
    try:
        if request.method == 'POST':
            setData = json.loads(request.body)
            getID = setData.get('Event ID')
            try: 
                userData = UserRegister.objects.get(user=request.user)
                getEventData = EventHandle.objects.get(id=getID, registeredUser=userData)
            except EventHandle.DoesNotExist as error:
                return JsonResponse({
                    'Message': f'Exception Caught: ---> No user Found:{str(error)}'
                })
            leftSeats = 0
            if(getEventData.userTicket.capacity + getEventData.seatingCapacity <= getEventData.userTicket.totalCapacity):
                leftSeats = getEventData.userTicket.capacity + getEventData.seatingCapacity
                getEventData.userTicket.capacity = leftSeats
                getEventData.userTicket.save()
                getEventData.delete()
            return JsonResponse({
                'Status': "Passed",
                'Message': "Successfully Cancelled the Event: {getEventData.userTicket.title} + Left Seats:{getEventData.userTicket.capacity}"
            })
    except json.JSONDecodeError as error:
        return JsonResponse({
            'Status': "Failed",
            'Message': f"Exception Caught: Error ---> {str(error)}"
        })
    return JsonResponse({
        'Message': 'URL is working'
    })


def event_update(request):
    pass

@csrf_exempt
@login_required
def event_delete(request):
    try:
        if request.method == 'GET':
            getRegisteredEventData = EventRegister.objects.filter()
            eventItems = []
        
            for item in getRegisteredEventData:
                eventItems.append({
                    'ID': item.id,
                    'Event Name': item.title
                })
            return JsonResponse({
                'Status': "Data Extracted:",
                'Message': eventItems
            })
        if request.method == 'POST':
            setData = json.loads(request.body)
            setEventID = setData.get('Event Id')
            getData = EventRegister.objects.get(id=setEventID)
            getData.delete()
            
            return JsonResponse({
                'Status': "Passed",
                'Message': "Deleted The Said Event successfully"
            })
    
    except json.JSONDecodeError as error:
        return JsonResponse({
            'Status': "Failed",
            'Message': f'Exception Caught: Error ---> {str(error)}'
        })
    
    return JsonResponse({
        'Status': "Passed",
        'Message': "URL is working"
        
    })
