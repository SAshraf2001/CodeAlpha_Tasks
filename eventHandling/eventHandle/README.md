<h1 align="center">&#128197; Event Handling - Core App (<code>eventHandle</code>)</h1>

<p>The <code>eventHandle</code> module is the primary engine of the Event Handling project. It manages the creation of events, user registrations, and capacity enforcement to ensure smooth event operations[cite: 1].</p>

<hr>

<h2>&#128161; Features</h2>
<ul>
    <li><strong>Event Creation &amp; Display:</strong> View details for upcoming events.</li>
    <li><strong>Capacity Tracking:</strong> Automatically tracks the total capacity of an event (<code>totalcapacity</code>) and manages registrations accordingly[cite: 1].</li>
    <li><strong>Business Logic Enforcement:</strong> Utilizes custom decorators to validate user states before allowing event registration[cite: 1].</li>
</ul>

<h2>&#128193; Key Components</h2>
<ul>
    <li><code>models.py</code>: Defines the schema for Events and Event Registrations[cite: 1].</li>
    <li><code>decorators.py</code>: Custom Python decorators used to restrict views and enforce application rules[cite: 1].</li>
    <li><code>migrations/0002_eventregister_totalcapacity.py</code>: Ensures events do not exceed their maximum allowed attendees[cite: 1].</li>
</ul>

<h2>&#128640; Usage</h2>
<p>Ensure database migrations are applied before interacting with event views:</p>
<pre><code>python manage.py migrate eventHandle</code></pre>
