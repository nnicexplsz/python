
import sqlite3 
conn = sqlite3.connect(r'E:\Chawadon_python\Project\Project1.db')
c = conn.cursor()
c.execute("""CREATE TABLE students (id integer PRIMARY KEY AUTOINCREMENT,
    Name varchar(30) NOT NULL,
    Level varchar(30) NOT NULL,
    Groupp varchar(2) NOT NULL,
    Field1 float NOT NULL,
    Field2 float NOT NULL,
    Field3 float NOT NULL,
    Field4 float NOT NULL,
    Field5 float NOT NULL,
    Field6 float NOT NULL,
    Field7 float NOT NULL,
    Field8 float NOT NULL,
    Field9 float NOT NULL,
    Field10 float NOT NULL,
    Scoresum varchar(30) NOT NULL,
    Typell varchar(30) NOT NULL)''')
conn.commit()
conn.close()