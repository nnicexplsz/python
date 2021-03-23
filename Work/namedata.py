import sqlite3
conn = sqlite3.connect("namedata.db")
c = conn.cursor()
c.execute ('''CREATE TABLE SQ2(id integer PRIMARY KEY AUTOINCREMENT,
    fname varchar(30) NOT NULL,
    lName varchar(30) NOT NULL,
    calss varchar(10) NOT NULL,
    competition varchar(30) NOT NULL,
    nametame varchar(30) NOT NULL)''')
conn.commit()
conn.close()


'''
import sqlite3
conn = sqlite3.connect("namedata.db")
c = conn.cursor()
def menu():
    global choice
    print('-'*5,'ระบบทะเบียนนักเรียน','-'*5)
    print('='*28,'\nเพิ่มข้อมูลสมัคร กด [a]\nแสดงข้อมูลนักเรียน [s]\nแก้ไขข้อมูลนักเรียน [e]\nลบข้อมูลนักเรียน [d]\nออกจากระบบ [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')

def add(fname,lName,calss,competition,nametame):
    try :
        conn = sqlite3.connect("namedata.db")
        c = conn.cursor()
        sql = '''INSERT INTO SQ2 (fname,lName,calss,competition,nametame) VALUES (?,?,?,?,?)'''
        data = (fname,lName,calss,competition,nametame)
        c.execute(sql,data)
        conn.commit()
        c.close()

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()
while True:
    menu()
    if choice == 's':
        show()
    elif choice == 'a':
        print("ต้องการออก กด exit")
        i = 11
        for i in range(10):
            a,b,c,d,e = input('ชื่อ-สกุล-คลาส-ประเภทการแข่งขัน-ชื่อทีม : ').split()
            add(a,b,c,d,e)
        n =(input('ต้องการออกจากระบบหรือไม่ [y/n]:'))
        if n == 'exit':
            print('ออกจากระบบเรียบร้อยแล้ว')
            break
        print('เพิ่มข้อมูลเรียบร้อยแล้ว')