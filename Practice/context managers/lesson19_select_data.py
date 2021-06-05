import sqlite3
from contextlib import contextmanager

@contextmanager
def db_open(db_name):
    name = sqlite3.connect(db_name)
    try:
        yield con
    finally:
        con.close()

con = sqlite3.connect('test.db')

cur = con.cursor()

data = cur.execute("SELECT * FROM stocks")

for record in data:
    print(record)

con.close()

with db_open(db_name='test.db') as con:
    con.write('Test context manager with generator')