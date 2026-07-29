<h1 align="center">&#128737;&#65039; Job Platform - Authentication App (<code>authenticationApp</code>)</h1>

<p>The <code>authenticationApp</code> is tailored specifically for the Job Platform project, managing the secure onboarding and authentication of different user types (e.g., Employers and Candidates)[cite: 1].</p>

<hr>

<h2>&#128736;&#65039; Core Responsibilities</h2>
<ul>
    <li><strong>Role-Based Authentication:</strong> Securely authenticates users interacting with the job board[cite: 1].</li>
    <li><strong>Session Management:</strong> Ensures state is maintained across the platform when users apply for jobs or post new listings[cite: 1].</li>
</ul>

<h2>&#128193; Key Components</h2>
<ul>
    <li><code>models.py</code>: Handles the specific user data requirements for the job board ecosystem[cite: 1].</li>
    <li><code>views.py</code>: Processes sign-in and sign-up requests[cite: 1].</li>
    <li><code>urls.py</code>: Defines the routing for identity verification[cite: 1].</li>
</ul>

<h2>&#128640; Setup</h2>
<pre><code>python manage.py makemigrations authenticationApp
python manage.py migrate</code></pre>
