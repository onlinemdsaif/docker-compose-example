from flask import Flask
import redis
import psycopg2

app = Flask(__name__)

# Connect to Redis
cache = redis.Redis(host='redis', port=6379)

# Connect to PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="mydatabase",
            user="myuser",
            password="mypassword",
            host="db"
        )
        return conn
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    db_conn = connect_db()
    if isinstance(db_conn, str):
        return f"Database connection error: {db_conn}"
    return "Hello, Docker Compose with Flask, Redis, and PostgreSQL!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
