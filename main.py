from database import cursor, db


def add_log(text, user):
    cursor.execute(
        f"INSERT INTO logs (text,user) VALUES ('{text}','{user}')"
    )
    db.commit()
    return cursor.lastrowid

def get_logs():
    cursor.execute("SELECT * FROM logs")
    return cursor.fetchall()

def get_log(id):
    cursor.execute(f"SELECT * FROM logs WHERE id = {id}")
    return cursor.fetchone()

def update_log(id, text, user):
    cursor.execute(
        f"UPDATE logs SET text = '{text}', user = '{user}' WHERE id = {id}"
    )
    db.commit()
    return cursor.rowcount

def delete_log(id):
    cursor.execute(f"DELETE FROM logs WHERE id = {id}")
    db.commit()
    return cursor.rowcount


delete_log(2)
