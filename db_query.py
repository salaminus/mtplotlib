import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

def query(data):
    cursor.execute(
        """SELECT * FROM stations
            WHERE year=? and month=? and day=?;""",
        data
    )
    # res = cursor.fetchone()
    # res = cursor.fetchmany(5)
    res = cursor.fetchall()
    print(res)