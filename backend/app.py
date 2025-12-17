from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Backend!", "status": "running"})

@app.route('/db')
def db_check():
    # Simple check to see if we can reach the DB
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "database"),
            database=os.getenv("DB_NAME", "testdb"),
            user=os.getenv("DB_USER", "user"),
            password=os.getenv("DB_PASS", "password")
        )
        return jsonify({"db_status": "Connected to Database Successfully!"})
    except Exception as e:
        return jsonify({"db_status": "Failed", "error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)