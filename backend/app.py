from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
# Enable CORS so the browser can call this API from the Frontend
CORS(app)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "database"),
        database=os.getenv("DB_NAME", "testdb"),
        user=os.getenv("DB_USER", "user"),
        password=os.getenv("DB_PASS", "password")
    )
    return conn

@app.route('/')
def home():
    return jsonify({"message": "Guestbook API Running"})

# 1. VIEW DATA (GET)
@app.route('/guests', methods=['GET'])
def get_guests():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT name, message FROM guestbook ORDER BY id DESC;')
        guests = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(guests)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. INSERT DATA (POST)
@app.route('/sign', methods=['POST'])
def sign_guestbook():
    try:
        data = request.json
        name = data.get('name')
        message = data.get('message')
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO guestbook (name, message) VALUES (%s, %s)', (name, message))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "message": "Signed successfully!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)