from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    db_url = os.environ.get('DATABASE_URL')
    try:
        conn = psycopg2.connect(db_url)
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Failed to connect to PostgreSQL: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
