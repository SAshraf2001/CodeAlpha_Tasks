import sqlite3
import string
import random
from flask import Flask, request, jsonify

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

# API Endpoint to create a short URL
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400
    
    conn = get_db_connection()
    short_id = generate_short_id()
    
    # Ensure unique short_id
    while conn.execute('SELECT * FROM urls WHERE short_url = ?', (short_id,)).fetchone() is not None:
        short_id = generate_short_id()
        
    conn.execute('INSERT INTO urls (original_url, short_url) VALUES (?, ?)', (original_url, short_id))
    conn.commit()
    conn.close()
    
    return jsonify({'short_url': f"{request.host_url}{short_id}"}), 201

# Endpoint to resolve the short URL
@app.route('/<short_id>', methods=['GET'])
def redirect_url(short_id):
    conn = get_db_connection()
    url_data = conn.execute('SELECT original_url FROM urls WHERE short_url = ?', (short_id,)).fetchone()
    conn.close()
    
    if url_data:
        # Returning a JSON response for the redirect or handled by frontend
        return jsonify({'original_url': url_data['original_url']}), 200
    else:
        return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True)