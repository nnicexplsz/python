import sqlite3
conn = sqlite3.connect('ProjectAA.db')
c = conn.cursor()
c.execute ('''CREATE TABLE covid (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    pas varchar(100) NOT NULL,
    age varchar(10) NOT NULL,
    sex vatchar(10) NOT NULL)''')
conn.commit()
conn.close()
