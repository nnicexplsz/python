import sqlite3
conn = sqlite3.connect("text.db")
c = conn.cursor()
c.execute('''CREATE TABLE covid19 ( id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    email varchar(100) NOT NULL,
    sex varchar(10) NOT NULL,
    age varchar(10) NOT NULL, )''')
conn.commit()
conn.close()