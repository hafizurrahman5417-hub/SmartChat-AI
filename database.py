import sqlite3

def init_db():
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            bot TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_chat(user, bot):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("INSERT INTO chats (user, bot) VALUES (?, ?)", (user, bot))
    conn.commit()
    conn.close()

def get_last_chats(limit=5):
    conn = sqlite3.connect("chat.db")
    c = conn.cursor()
    c.execute("SELECT user, bot FROM chats ORDER BY id DESC LIMIT ?", (limit,))
    data = c.fetchall()
    conn.close()
    return data[::-1]