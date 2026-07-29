<h1 align="center">&#128188; Job Platform - Job Posting App (<code>jobPosting</code>)</h1>

<p>The <code>jobPosting</code> application forms the backbone of the Job Platform. It handles the entire lifecycle of a job board&mdash;from an employer creating a listing to a candidate submitting an application with a resume[cite: 1].</p>

<hr>

<h2>&#128161; Features</h2>
<ul>
    <li><strong>Comprehensive Listings:</strong> Supports detailed job attributes including <code>ExperienceLevel</code>, <code>EmployeeType</code>, and <code>JobStatus</code>[cite: 1].</li>
    <li><strong>Application Tracking:</strong> Monitors applicant submissions and timestamps using <code>TrackJobApplication</code> and <code>JobApply</code> models[cite: 1].</li>
    <li><strong>Media Management:</strong> Securely handles the upload and storage of candidate resumes (PDFs) and profile pictures (JPEGs)[cite: 1].</li>
    <li><strong>Access Protection:</strong> Uses custom decorators to ensure only authorized users can apply for or manage postings[cite: 1].</li>
</ul>

<h2>&#128193; Key Components</h2>
<ul>
    <li><code>models.py</code>: Defines complex relationships between Job Postings, Applicants, and Employee Types[cite: 1].</li>
    <li><code>decorators.py</code>: Enforces role-based access control on specific views[cite: 1].</li>
    <li><code>migrations/</code>: Contains iterative updates, including the addition of <code>JobApply</code> and application tracking features[cite: 1].</li>
</ul>

<h2>&#128640; Media Configuration</h2>
<p>This app handles file uploads. Ensure your main <code>settings.py</code> is configured for media routing:</p>
<pre><code>MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')</code></pre>
