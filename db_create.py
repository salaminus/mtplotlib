import sqlite3


conn = sqlite3.connect('bd.db')
cursor = conn.cursor()
# станция, год, месяц, день, час, напр ветра, осадки, темпер-ра, влажность
cursor.execute("""CREATE TABLE IF NOT EXISTS stations(
    idstations INT PRIMARY KEY,
    stname TEXT,
    year INT,
    month INT,
    day INT,
    hour INT,
    dirwind TEXT,
    precipit REAL,
    temperature REAL,
    humidity REAL);"""
    )
conn.commit()

# Добавление записей в БД:
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
                         2,
                         '20046',
                         '1966',
                         '12',
                         '31',
                         '23',
                         '3',
                         '10.0',
                         '-30.0',
                         '70.0'
                     );
"""