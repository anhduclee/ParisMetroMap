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
                    weight REAL,
                    FOREIGN KEY (source) REFERENCES nodes(id),
                    FOREIGN KEY (target) REFERENCES nodes(id),
                    PRIMARY KEY (source, target, line)
                )
            """)
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()

def select_table(table: str):
    conn = None
    try:
        conn = sqlite3.connect("database.db")
        with conn:
            cursor = conn.cursor()
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()

def insert_data():
    with open("graph.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    nodes = data["nodes"]
    edges = data["edges"]

    conn = None
    try:
        conn = sqlite3.connect("database.db")
        with conn:
            cursor = conn.cursor()
            for (key, value) in nodes.items():
                cursor.execute("""
                    INSERT INTO nodes (id, name, latitude, longitude) VALUES
                        (?,?,?,?)""", 
                    (key, value["name"], value["latitude"], value["longitude"]))
            for (key, value) in edges.items():
                for edge_detail in value:
                    cursor.execute("""
                        INSERT INTO edges(source, target, line, color) VALUES
                            (?,?,?,?)""",
                    (key, edge_detail["target"], edge_detail["line"], edge_detail["color"]))

    except Exception as err:
        print(err)
    finally:
        if conn:
            conn.close()

