import sqlite3


conn = sqlite3.connect('bd.db')
cursor = conn.cursor()
def add_sign(counter, temp):
    cursor.execute(
        """
                    INSERT INTO stations (
                                 idstations,
                                 stname,
                                 year,
                                 month,
                                 day,
                                 hour,
                                 dirwind,
                                 precipit,
                                 temperature,
                                 humidity
                             )
                             VALUES (
                                 ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
                             );
        """, (counter,
              temp[0],
              temp[5],
              temp[6],
              temp[7],
              temp[10],
              float(temp[39]),
              float(temp[47]),
              float(temp[-31]),
              float(temp[-15]))
    )
    conn.commit()
