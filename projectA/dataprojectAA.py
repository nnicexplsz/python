import sqlite3
conn = sqlite3.connect('ProjectAA.db')
c = conn.cursor()
c.execute ('''CREATE TABLE covidIII (id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lname varchar(30) NOT NULL,
    pas varchar(100) NOT NULL,
    ps1 varchar(30) NOT NULL,
    ps2 varchar(30) NOT NULL,
    ps3 varchar(30) NOT NULL,
    ps4 vatchar(30) NOT NULL,
    ps5 vatchar(30) NOT NULL,
    ps6 vatchar(30) NOT NULL,
    ps7 vatchar(30) NOT NULL,
    ps8 vatchar(30) NOT NULL)''')
conn.commit()
conn.close()