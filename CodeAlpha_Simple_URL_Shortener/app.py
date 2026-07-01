import sqlite3
import string
import random
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT NOT NULL, short_url TEXT NOT NULL UNIQUE)')
    conn.commit()
    conn.close()

def generate_short_id(num_of_chars=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=num_of_chars))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        if not url:
            return render_template('index.html', error='Please enter a URL.')
        
        conn = get_db_connection()
        short_id = generate_short_id()
        
        while conn.execute('SELECT * FROM urls WHERE short_url = ?', (short_id,)).fetchone() is not None:
            short_id = generate_short_id()
            
        conn.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (url, short_id))
        conn.commit()
        conn.close()
        
        short_url = request.host_url + short_id
        return render_template('index.html', short_url=short_url)
    
    return render_template('index.html')

@app.route('/<short_id>')
def redirect_url(short_id):
    conn = get_db_connection()
    url_data = conn.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_id,)).fetchone()
    conn.close()
    
    if url_data:
        return redirect(url_data['original_url'])
    else:
        return 'URL not found', 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
