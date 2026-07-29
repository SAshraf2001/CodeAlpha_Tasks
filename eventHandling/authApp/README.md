<h1 align="center">&#128272; Event Handling - Authentication App (<code>authApp</code>)</h1>

<p>This Django application serves as the security and identity management module for the Event Handling system. It is responsible for handling user registration, authentication, and session management[cite: 1].</p>

<hr>

<h2>&#128736;&#65039; Core Responsibilities</h2>
<ul>
    <li><strong>User Identity:</strong> Manages user models, profile creation, and secure credential storage[cite: 1].</li>
    <li><strong>Access Control:</strong> Validates user sessions and restricts unauthorized access to event management features[cite: 1].</li>
</ul>

<h2>&#128193; Key Components</h2>
<ul>
    <li><code>models.py</code>: Defines the database schema for user profiles[cite: 1].</li>
    <li><code>views.py</code>: Contains the logic for login, registration, and logout workflows[cite: 1].</li>
    <li><code>urls.py</code>: Maps the authentication endpoints for the application[cite: 1].</li>
    <li><code>migrations/</code>: Tracks schema changes related to user identities[cite: 1].</li>
</ul>

<h2>&#128640; Integration</h2>
<p>This app is designed to work in tandem with the <code>eventHandle</code> app. Ensure that <code>authApp</code> is added to your <code>INSTALLED_APPS</code> in the main <code>settings.py</code> file[cite: 1].</p>
<pre><code>python manage.py makemigrations authApp
python manage.py migrate</code></pre>
