import sqlite3
import random
import string
import pandas as pd

conn = sqlite3.connect('local_database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS titanic (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    surname TEXT,
                    seat TEXT,
                    class INTEGER,
                    bought_ticket_date TEXT,
                    birthdate TEXT,
                    disabilities INTEGER,
                    disabilities_spec TEXT,
                    job TEXT
                )''')

for _ in range(100):
    name = ''.join(random.choices(string.ascii_uppercase, k=5))
    surname = ''.join(random.choices(string.ascii_uppercase, k=5))
    seat = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))
    class_level = random.randint(1, 3)
    bought_ticket_date = ''.join(random.choices(string.digits, k=8))
    birthdate = ''.join(random.choices(string.digits, k=8))
    disabilities = random.randint(0, 1)
    disabilities_spec = 'Examples of disabilities' if disabilities == 1 else ''
    job = ''.join(random.choices(string.ascii_lowercase, k=7))

    cursor.execute('''INSERT INTO titanic 
                      (name, surname, seat, class, bought_ticket_date, birthdate, disabilities, disabilities_spec, job) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (name, surname, seat, class_level, bought_ticket_date, birthdate, disabilities, disabilities_spec,
                    job))
conn.commit()
conn.close()

conn = sqlite3.connect('local_database.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM titanic")
print("Records from schema1_table1:")
example = pd.DataFrame(cursor.fetchall())
print(example)

conn.commit()
conn.close()

