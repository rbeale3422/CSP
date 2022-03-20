import sqlite3
from sqlite3.dbapi2 import OperationalError

# create connection object to database (if does not exist will create)
con = sqlite3.connect('test.db')

cur = con.cursor()

try:
    # create a table
    cur.execute('''CREATE TABLE stocks
                (date text, trans text, symbol text, qty real, price real)''')
except OperationalError as error:
    print(error)

# insert a record into the database
cur.execute("INSERT INTO stocks VALUES ('2006-01-05', 'BUY', 'RHAT', 100, 35.14)")

# save and commit changes to database
con.commit()

# close the connection
con.close()