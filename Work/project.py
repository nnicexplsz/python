
import sqlite3
conn = sqlite3.connect("project.db")
c = conn.cursor()
'''
c.execute ('''CREATE TABLE project (id integer PRIMARY KEY AUTOINCREMENT,
    Fname varchar(30) NOT NULL,
    LName varchar(30) NOT NULL,
    score float(30) NOT NULL,
    time float(30) NOT NULL,
    sum float(30) NOT NULL)''')
conn.commit()
conn.close()
'''