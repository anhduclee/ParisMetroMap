import sqlite3
import json
import os

def init_db():
    if os.path.exists("database.db"):
        os.remove("database.db")
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        conn.execute("PRAGMA foreign_keys = ON")
        with conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE nodes (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    latitude REAL,
                    longitude REAL,
                    is_active INTEGER DEFAULT 1
                )
            """)
            cursor.execute("""
                CREATE TABLE edges (
                    source TEXT,
                    target TEXT,
                    line TEXT,
                    color TEXT,
                    is_active INTEGER DEFAULT 1,
                    FOREIGN KEY (source) REFERENCES nodes(id),
                    FOREIGN KEY (target) REFERENCES nodes(id)
                )
            """)
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()

def insert_data():
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        with conn:
            pass
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()