import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "tracezero.db")

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                broker      TEXT,
                broker_type TEXT,
                url         TEXT,
                raw_text    TEXT,
                pii_found   TEXT,
                match_score REAL,
                status      TEXT DEFAULT 'Found',
                created_at  TEXT
            )
        """)
        conn.commit()
    print("✅ Database initialized.")

def insert_record(broker, broker_type, url, raw_text, pii_found, match_score):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO records (broker, broker_type, url, raw_text, pii_found, match_score, status, created_at)
            VALUES (?, ?, ?, ?, ?, ?, 'Found', ?)
        """, (broker, broker_type, url, raw_text, str(pii_found), match_score,
              datetime.now().isoformat()))
        conn.commit()

def get_all_records():
    with get_connection() as conn:
        rows = conn.execute("SELECT * FROM records ORDER BY id DESC").fetchall()
    return rows

def update_status(record_id: int, new_status: str):
    with get_connection() as conn:
        conn.execute("UPDATE records SET status=? WHERE id=?", (new_status, record_id))
        conn.commit()
