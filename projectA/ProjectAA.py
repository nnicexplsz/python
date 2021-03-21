import sqlite3
conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
c = conn.cursor()
# c.execute ('''CREATE TABLE covid (id integer PRIMARY KEY AUTOINCREMENT,
#     fname varchar(30) NOT NULL,
#     lname varchar(30) NOT NULL,
#     pas varchar(100) NOT NULL,
#     age varchar(10) NOT NULL,
#     sex vatchar(10) NOT NULL)''')
conn.commit()
conn.close()
information = ["Open","Standard","Modify","Standard manual"]


def menu():
    global choice
    print('-'*5,'ระบบลงทะเบียนอาการเสี่ยง COVID-19','-'*5)
    print('='*28,'\nเพิ่มข้อมูลของท่าน           กด [a]\nแสดงข้อมูลผู้เสี่ยง COVID-19  กด [s]\nแก้ไขข้อมูลผู้เสี่ยง COVID-19  กด [e]\nลบข้อมูลผู้เสี่ยง   COVID-19  กด [d]\nออกจากระบบ              กด [x]')
    choice = input('\nกรุณาเลือกทำรายการ :')

def add(fname,lname,pas,sex,age):
    try :
        conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
        c = conn.cursor()
        sql = '''INSERT INTO covid (fname,lname,pas,age,sex) VALUES (?,?,?,?,?)'''
        data = (fname,lname,pas,age,sex)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()


def show():
    conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM covid''')
    result = c.fetchall()
    print("-"*75)
    print('{0:<12}{1:<15}{2:<15}{3:<26}{4:<12}{5}'.format('ลำดับที่',' ชื่อ','สกุล','เลขบัตรประจำตัวประชาชน','อายุ','เพศ'))
    print("-"*75)
    for x in result :
        print('{0:<8}{1:<15}{2:<15}{3:<22}{4:<11}{5}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
    print('ทำรายการเสร็จสิ้น\n')
    conn.commit()
    conn.close()

def edit(fname,lname,pas,age,sex,iid):
    conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
    c = conn.cursor()
    try :
        data = (fname,lname,pas,age,sex,'{}'.format(iid))
        c.execute('''UPDATE covid SET fname =?, lname =?, pas =?, age =?, sex =?  ''',data)
        conn.commit()
        c.close()
        print('แก้ไขข้อมูลเรียบร้อย\n')
        
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

def delete(del_id):
    conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
    c = conn.cursor()
    try :
        c.execute('DELETE FROM covid WHERE id = {}'.format(del_id))
        conn.commit()
        c.close()
        print('ลบข้อมูลเรียบร้อย\n')       

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

while True:
    menu()       
    if choice == 'a':
        fn,ln,ps,s,a = input('ชื่อ---สกุล---เลขบัตรประจำตัวประชาชน---อายุ---เพศ : ').split()
        add(fn,ln,ps,s,a)
    elif choice == 's':
        show()
    elif choice == 'e':
        iid = input('เลือกลำดับที่ต้องการแก้ไข : ')
        efn,eln,ps,ea,es = input('ชื่อ---สกุล---เลขบัตรประจำตัวประชาชน---อายุ---เพศ : ').split()
        edit(efn,eln,ps,ea,es,iid)
    elif choice == 'd':
        del_id = input('เลือกลำดับที่ต้องการลบ : ')
        delete(del_id)

    elif choice == 'x':
        yesno = input('ต้องการออกจากระบบหรือไม่ [y/n]: ')
        if yesno == 'Y' or yesno == 'y':
            print('ออกจากระบบเรียบร้อยแล้ว')
            break
        elif yesno == 'N' or yesno == 'n':
            print('ได้ทำการกลับสู่ระบบแล้ว')
            continue
        else:
            print('เสร็จสิ้นการทำรายการ')
'''"""reset"""    

DELETE FROM students;
DELETE FROM sqlite_sequence WHERE name = 'covid'
'''







'''
def input_date():
    print("อาการของคุณ")
    f=input("มีไข้ สูงกว่า 37.5 องศาเซลเซียส (Y/N) :")
    if (f=='Y'):
        scor += 1

    a=input("มีไข้หรือไม่ (Y/N) :")
    if (a=='Y'):
        scor += 1

    b=input("ไอแห้งหรือไม่ (Y/N) :")
    if (b=='Y'):
        scor += 1

    c=input("ไอมีเสมหะหรือไม่ (Y/N) :")
    if (c=='Y'):
        scor += 1

    d=input("เจ็บคอหรือไม่ (Y/N) :")
    if (d=='Y'):
        scor += 1

    e=input("มีน้ำมูกหรือไม่ (Y/N) :")
    if (e=='Y'):
        scor += 1

    g=input("ปวดกล้ามเนื้อ (Y/N) :")
    if (g=='Y'):
        scor += 1

    h=input("อ่อนเพลีย (Y/N) :")
    if (h=='Y'):
        scor += 1

    print(scor)

'''