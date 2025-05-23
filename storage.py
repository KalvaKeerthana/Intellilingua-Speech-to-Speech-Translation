import sqlite3
from datetime import datetime

def create_table():
    # Connect to DB (creates file if not exist)
    conn= sqlite3.connect('conversations.db')
    cursor= conn.cursor()

    # Create Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS conversations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_text TEXT,
        translated_text TEXT,         
        source_lang TEXT,
        target_lang TEXT,
        original_audio_path TEXT,
        translated_audio_path TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )

    ''')
    
    conn.commit()
    conn.close()


# insert or save a conversation
def save_conversations(original, translated, src_lang, tgt_lang, orig_audio_path, trans_audio_path):
    conn=sqlite3.connect('conversations.db')
    cursor=conn.cursor()

    cursor.execute('''
        INSERT INTO conversations
        (original_text, translated_text, source_lang, target_lang, original_audio_path, translated_audio_path)
        VALUES (?,?,?,?,?,?)
    ''' ,(original, translated, src_lang, tgt_lang, orig_audio_path, trans_audio_path)
    )
    conn.commit()
    conn.close()



#view all stores conversations
def view_conversations():
    conn = sqlite3.connect('conversations.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM conversations")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()



if __name__ == "__main__":
    create_table()
    save_conversations("Hello", "Bonjour", "en", "fr", "recordings/original_hello.wav",
    "recordings/translated_bonjour.wav")
    view_conversations()


   
    

