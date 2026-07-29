<h1 align="center">&#128279; Simple URL Shortener</h1>

<p>A lightweight and efficient web application designed to convert long, cumbersome URLs into concise, easily shareable links. This project demonstrates foundational backend routing and database management[cite: 1].</p>

<hr>

<h2>&#128736;&#65039; Tech Stack</h2>
<ul>
    <li><strong>Language:</strong> Python[cite: 1]</li>
    <li><strong>Database:</strong> SQLite[cite: 1]</li>
    <li><strong>Architecture:</strong> Monolithic</li>
</ul>

<h2>&#128193; Repository Structure</h2>
<ul>
    <li><code>app.py</code>: The core application file handling routing and URL redirection logic[cite: 1].</li>
    <li><code>database.db</code>: The SQLite database storing the mapping between original URLs and their shortened counterparts[cite: 1].</li>
</ul>

<h2>&#128640; Getting Started</h2>
<ol>
    <li><strong>Clone the repository</strong> and navigate to the project folder.</li>
    <li><strong>Run the application:</strong>
        <pre><code>python app.py</code></pre>
    </li>
    <li><strong>Access the app</strong> via your local server (typically <code>http://127.0.0.1:5000/</code>).</li>
</ol>

<h2>&#128161; Features</h2>
<ul>
    <li><strong>URL Generation:</strong> Instantly generate a shortened URL for any valid web address.</li>
    <li><strong>Persistent Storage:</strong> Safely stores all URL mappings in a local SQLite database for consistent redirection[cite: 1].</li>
</ul>
