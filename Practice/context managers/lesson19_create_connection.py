import sqlite3

class Connect_data:
    def __init__(self, name, mode='r'):
        self.name = name
    def __enter__(self):
        self.con = sqlite3.connect(self.name)
        return self.con
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.con.close()


with Connect_data('test.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE stocks
               (date text, trans text, symbol text, qty real, price real)''')
    cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
    con.commit()


