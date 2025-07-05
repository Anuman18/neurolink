import sqlite3
from datetime import datetime

conn = sqlite3.connect("emotion_logs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS emotions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    source TEXT,
    emotion TEXT,
    timestamp TEXT
)
""")
conn.commit()

def log_emotion(source, emotion):
    cursor.execute("""
        INSERT INTO emotions (source, emotion, timestamp)
        VALUES (?, ?, ?)
    """, (source, emotion, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()

def get_emotion_logs():
    cursor.execute("SELECT source, emotion, timestamp FROM emotions ORDER BY id DESC")
    return cursor.fetchall()
