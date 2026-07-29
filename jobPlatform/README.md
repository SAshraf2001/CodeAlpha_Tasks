<h1 align="center">&#128188; Job Platform Project</h1>

<p>Welcome to the <strong>Job Platform</strong> repository! This is a robust, Django-based job board application designed to connect employers with potential candidates. It features comprehensive job listing management, secure applicant tracking, and role-based access control[cite: 1].</p>

<hr>

<h2>&#128161; Key Features</h2>
<ul>
    <li><strong>Role-Based Authentication:</strong> Distinct workflows and access levels for Employers and Candidates, managed securely[cite: 1].</li>
    <li><strong>Job Management:</strong> Employers can post jobs detailing <code>ExperienceLevel</code>, <code>EmployeeType</code>, and track the <code>JobStatus</code>[cite: 1].</li>
    <li><strong>Applicant Tracking System (ATS):</strong> Candidates can apply to jobs, and their applications are tracked dynamically using <code>JobApply</code> and timestamped logging[cite: 1].</li>
    <li><strong>Media &amp; File Handling:</strong> Secure storage and retrieval of user profile pictures (JPEGs) and candidate resumes (PDFs)[cite: 1].</li>
    <li><strong>Custom View Protection:</strong> Specialized Python decorators ensure that only authorized roles can access specific views[cite: 1].</li>
</ul>

<hr>

<h2>&#128193; Project Structure</h2>
<p>The system is built using a modular Django architecture, divided into distinct applications:</p>
<ul>
    <li><strong><code>authenticationApp/</code></strong>: Handles all user identity operations, including login, registration, role assignment, and session management[cite: 1].</li>
    <li><strong><code>jobPosting/</code></strong>: The core engine of the platform. Manages the creation of job listings, processing of candidate applications, and database schema for employee types and job statuses[cite: 1].</li>
    <li><strong><code>jobPlatform/</code></strong>: The main Django configuration directory containing settings, root URL routing, and WSGI/ASGI configurations[cite: 1].</li>
    <li><strong><code>media/</code></strong>: The local directory structured to handle user-uploaded files, specifically organized into <code>profile_pics/</code>, <code>resumes/</code>, and <code>supportDocs/</code>[cite: 1].</li>
</ul>

<hr>

<h2>&#128736;&#65039; Tech Stack</h2>
<ul>
    <li><strong>Backend Framework:</strong> Python, Django</li>
    <li><strong>Database:</strong> SQLite (Default)</li>
    <li><strong>Architecture:</strong> MVT (Model-View-Template)</li>
</ul>

<hr>

<h2>&#128640; Getting Started</h2>

<h3>Prerequisites</h3>
<p>Ensure you have the following installed:</p>
<ul>
    <li>Python 3.x</li>
    <li><code>pip</code> (Python package manager)</li>
</ul>

<h3>Installation &amp; Setup</h3>
<ol>
    <li>
        <strong>Clone the repository and navigate to the project directory:</strong>
        <pre><code>git clone &lt;your-repository-url&gt;
cd CodeAlpha_Tasks/jobPlatform</code></pre>
    </li>
    <li>
        <strong>Create and activate a virtual environment (Recommended):</strong>
        <pre><code>python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate</code></pre>
    </li>
    <li>
        <strong>Install the dependencies:</strong>
        <pre><code>pip install django</code></pre>
        <em>Note: If you add more dependencies (like Pillow for image handling), ensure you install them or generate a <code>requirements.txt</code>.</em>
    </li>
    <li>
        <strong>Apply database migrations:</strong>
        <p>This will set up the tables for both the <code>authenticationApp</code> and <code>jobPosting</code> models[cite: 1].</p>
        <pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>
    </li>
    <li>
        <strong>Start the development server:</strong>
        <pre><code>python manage.py runserver</code></pre>
    </li>
    <li>
        <strong>Access the Application:</strong> Open your web browser and navigate to <code>http://127.0.0.1:8000/</code>.
    </li>
</ol>

<hr>

<h2>&#128221; License</h2>
<p>Distributed under the MIT License. See <code>LICENSE</code> for more information.</p>
