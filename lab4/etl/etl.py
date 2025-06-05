import psycopg2
import requests
import time

DB_PARAMS = {
    "host": "host.docker.internal",
    "database": "mltest",
    "user": "mluser",
    "password": "mlpassword"
}
API_URL = "http://api:8000/predict"

def wait_for_db():
    for _ in range(30):
        try:
            conn = psycopg2.connect(**DB_PARAMS)
            conn.close()
            return
        except:
            time.sleep(2)
    raise Exception("Database not available")

wait_for_db()

conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

cur.execute("SELECT id, text FROM input_data WHERE id NOT IN (SELECT id FROM output_data)")
rows = cur.fetchall()

for row in rows:
    id_, text = row
    resp = requests.post(API_URL, json={"text": text})
    prediction = resp.json().get("prediction", "")
    cur.execute("INSERT INTO output_data (id, text, prediction) VALUES (%s, %s, %s)", (id_, text, prediction))
    conn.commit()

cur.close()
conn.close()
