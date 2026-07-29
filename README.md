<h1 align="center">CodeAlpha Tasks</h1>

<p>Welcome to the <strong>CodeAlpha Tasks</strong> repository. This project contains a collection of web applications developed to demonstrate backend development, routing, database management, and authentication using Python frameworks[cite: 1].</p>

<hr>

<h2>&#128193; Repository Structure</h2>
<p>This repository is organized into three distinct projects:</p>

<h3>1. Simple URL Shortener</h3>
<p>A lightweight web application designed to take long, cumbersome URLs and convert them into short, easily shareable links.</p>
<ul>
    <li><strong>Core Technologies:</strong> Python, SQLite (via <code>database.db</code>)[cite: 1].</li>
    <li><strong>Key Files:</strong> <code>app.py</code>, <code>database.db</code>[cite: 1].</li>
</ul>

<h3>2. Event Handling System</h3>
<p>A comprehensive Django-based application built to manage event registrations and user authentication[cite: 1].</p>
<ul>
    <li><strong>Core Technologies:</strong> Python, Django.</li>
    <li><strong>Key Modules:</strong>
        <ul>
            <li><code>authApp</code>: Handles user registration, login, and access control[cite: 1].</li>
            <li><code>eventHandle</code>: Manages event creation, display, and capacity tracking[cite: 1].</li>
        </ul>
    </li>
</ul>

<h3>3. Job Platform</h3>
<p>A robust Django application serving as a job board where employers can post opportunities and candidates can apply.</p>
<ul>
    <li><strong>Core Technologies:</strong> Python, Django.</li>
    <li><strong>Key Modules:</strong>
        <ul>
            <li><code>authenticationApp</code>: Manages user accounts and role-based access[cite: 1].</li>
            <li><code>jobPosting</code>: Handles the creation of job listings, application tracking, and resume/profile picture uploads[cite: 1].</li>
        </ul>
    </li>
</ul>

<hr>

<h2>&#128640; Getting Started</h2>
<p>To get a local copy up and running, follow these simple steps.</p>

<h3>Prerequisites</h3>
<p>Ensure you have the following installed on your local machine:</p>
<ul>
    <li><a href="https://www.python.org/downloads/" target="_blank">Python 3.x</a></li>
    <li><code>pip</code> (Python package installer)</li>
    <li><code>virtualenv</code> (Recommended for isolating project dependencies)</li>
</ul>

<h3>Installation</h3>
<ol>
    <li>
        <strong>Clone the repository</strong>
        <pre><code>git clone https://github.com/your-username/CodeAlpha_Tasks.git
cd CodeAlpha_Tasks</code></pre>
    </li>
    <li>
        <strong>Set up a virtual environment</strong> (Optional but highly recommended)
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`</code></pre>
    </li>
    <li>
        <strong>Install Dependencies</strong>
        <p>Navigate to the specific project directory you wish to run and install the required packages. <em>(Note: Ensure you have a <code>requirements.txt</code> generated for your apps, or install Django/Flask manually as needed)</em>.</p>
        <pre><code>pip install django flask</code></pre>
    </li>
</ol>

<hr>

<h2>&#128187; Running the Applications</h2>

<h3>Running the Simple URL Shortener</h3>
<ol>
    <li>Navigate to the URL Shortener directory:
        <pre><code>cd CodeAlpha_Simple_URL_Shortener</code></pre>
    </li>
    <li>Run the application:
        <pre><code>python app.py</code></pre>
    </li>
</ol>

<h3>Running the Django Projects (Event Handling / Job Platform)</h3>
<p>Both the Event Handling and Job Platform projects follow standard Django execution commands[cite: 1].</p>
<ol>
    <li>Navigate to the desired project directory (e.g., <code>eventHandling</code> or <code>jobPlatform</code>):
        <pre><code>cd eventHandling  # or cd jobPlatform</code></pre>
    </li>
    <li>Apply database migrations:
        <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
    </li>
    <li>Start the development server:
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>Open your browser and navigate to <code>http://127.0.0.1:8000/</code>.</li>
</ol>

<hr>

<h2>&#128736;&#65039; Built With</h2>
<ul>
    <li><strong>Backend:</strong> Python, Django, Flask (Assumed for <code>app.py</code> URL Shortener)</li>
    <li><strong>Database:</strong> SQLite</li>
    <li><strong>Architecture:</strong> MVT (Model-View-Template) for Django projects</li>
</ul>

<hr>

<h2>&#128221; License</h2>
<p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>
