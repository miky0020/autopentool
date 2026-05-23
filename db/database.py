import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'results.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS findings (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            target    TEXT,
            module    TEXT,
            finding   TEXT,
            severity  TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("[*] Database initialized.")

def save_finding(data):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO findings (target, module, finding, severity) VALUES (?,?,?,?)",
        (data.get('target'), data.get('module'), data.get('finding'), data.get('severity'))
    )
    conn.commit()
    conn.close()

def get_all_findings():
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute("SELECT * FROM findings ORDER BY timestamp DESC").fetchall()
    conn.close()
    return rows
