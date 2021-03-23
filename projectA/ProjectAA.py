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
# information = ["Open","Standard","Modify","Standard manual"]

#เมนู
def menu(): 
    global choice
    print('-'*5,'ระบบลงทะเบียนอาการเสี่ยง COVID-19','-'*5)
    print('='*35,'\nกรอกประวัติส่วนตัวของท่าน         กด [a] |\nกรอกข้อมูลผู้เสี่ยง      COVID-19  กด [g] |\nแก้ไขประวัติผู้เสี่ยง     COVID-19  กด [e] |\nแก้ไขข้อมูลผู้เสี่ยง      COVID-19  กด [h] |\nแสดงข้อมูลผู้เสี่ยง      COVID-19  กด [s] |')
    print('='*35,'\nลบข้อมูลผู้เสี่ยง        COVID-19  กด [d] |\nออกจากระบบ                   กด [x] |')
    print('='*35)
    choice = input('\nกรุณาเลือกทำรายการ :')

#เพิ่มรายชื่อเข้าตารางประวัติของผู้ป่วย
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

#รายชื่อตารางประวัติผู้ป่วย ดึงข้อมูลไปตารางข้อมูลผู้ป่วย
def imformationpeople(fname,lname,pas): 
    try :
        conn = sqlite3.connect (r'E:\Chawadon_python\ProjectAA.db')
        c = conn.cursor()
        c.execute("SELECT id,fname,lname,pas FROM covid")
        rows = c.fetchall()
        for row in rows:
            a1 = row[0]
            a2 = row[1]
            a3 = row[2]
            a3 = row[3]
        print(a1,a2,a3,a4) 
    except sqlite3.Error as e :
        print(e)

  



   #โชว์ตารางประวัติส่วนตัวของผู้ป่วย   

#โชว์ตารางประวัติของผู้ป่วย
def show():
    conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM covid''') #SELECT STAR FROM โขว์ทั้งหมดในหน้าจอ
    result = c.fetchall()
    print("-"*75)
    print('{0:<12}{1:<15}{2:<15}{3:<26}{4:<12}{5}'.format('ลำดับที่',' ชื่อ','สกุล','เลขบัตรประจำตัวประชาชน','อายุ','เพศ'))
    print("-"*75)
    for x in result :
        print('{0:<8}{1:<15}{2:<15}{3:<22}{4:<11}{5}'.format(x[0],x[1],x[2],x[3],x[4],x[5]))
    print('ทำรายการเสร็จสิ้น\n')
    conn.commit()
    conn.close() 

#โชว์ตารางข้อมูลผู้ป่วย
def show2():
    conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM covidIII''')
    result = c.fetchall()
    print("-"*150)
    print('{0:<14}{1:<19}{2:<16}{3:<16}{4:<16}{5:<8}{6:<10}{7:<10}{8:<8}{9:<9}{10:<11}{11:<10}{10}'.format('ลำดับที่ |','ชื่อ |','นามสกุล |','เลขประจำตัวประชาชน |','อณุหภูมิสูงกว่า 37.5ํ |',' มีไข้ |','ไอแห้ง |','ไอมีเสมหะ |','เจ็บคอ |','มีน้ำมูก |','ปวดกล้ามเนื้อ |','อ่อนเพลีย |'))
    print("-"*150)
    for x in result :
        print('{0:<10}{1:<16}{2:<16}{3:<25}{4:<14}{5:<6}{6:<10}{7:<10}{8:<8}{9:<9}{10:<11}{11:<10}{10}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11]))
    print('ทำรายการเสร็จสิ้น\n')
    conn.commit()
    conn.close()

#แก้ไขประวัติส่วนตัวของผู้ป่วย
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

#กรอกข้อมูลของผู้ป่วย
def imformation(fname,lname,pas,ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8):
    try :
        conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
        c = conn.cursor()
        sql = '''INSERT INTO covidIII (fname,lname,pas,ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''
        data = (fname,lname,pas,ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8)
        c.execute(sql,data)
        conn.commit()
        c.close()
        print('เพิ่มข้อมูลเรียบร้อย')

    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()  

#การแก้ไขข้อมูลในตารางผู้ป่วย
def editimformation(ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8): 
    conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
    c = conn.cursor()
    try :
        data = (ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8)
        c.execute('''UPDATE covidIII SET ps1 =?, ps2 =?, ps3 =?, ps4 =?, ps5 =?, ps6 =?, ps7=?, ps8 =?  ''',data)
        conn.commit()
        c.close()
        print('แก้ไขข้อมูลเรียบร้อย\n')
        
    except sqlite3.Error as e :
        print(e)
    finally :
        if conn :
            conn.close()

#การลบข้อมูลในตารางของผู้ป่วย
def delete(): 
    number = input('เลือกลำดับที่ต้องการลบ : ')
    try :
        conn = sqlite3.connect(r'E:\Chawadon_python\ProjectAA.db')
        c = conn.cursor()
        c.execute('DELETE FROM covidIII WHERE id = ?',number)
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
    if choice == 'a': #กรอกประวัติส่วนตัวของท่าน
        fn = input('ชื่อ :')
        ln = input('นามสกุล :')
        ps = input('เลขบัตรประจำตัวประชาชน :')
        a = input('เพศ :')
        s = input('อายุ :')
        add(fn,ln,ps,a,s)

    elif choice == 's': #แสดงข้อมูลผู้เสี่ยง      COVID-19
        show()
        show2()

    elif choice == 'e': #แก้ไขประวัติผู้เสี่ยง     COVID-19
        iid = input('เลือกลำดับที่ต้องการแก้ไข : ')
        efn = input('ชื่อ :')
        eln = input('นามสกุล :')
        ps = input('เลขบัตรประจำตัวประชาชน :')
        ea = input('เพศ :')
        es = input('อายุ :') 
        edit(efn,eln,ps,ea,es,iid)

    elif choice == 'g': #กรอกข้อมูลผู้เสี่ยง      COVID-19   
        global maa,mab,mac,mad,mae,maf,mag,mah,sum
        try :
            conn = sqlite3.connect (r'E:\Chawadon_python\ProjectAA.db')
            c = conn.cursor()
            c.execute("SELECT id,fname,lname,pas FROM covid")
            rows = c.fetchall()
            for row in rows:
                a1 = row[0]
                a2 = row[1]
                a3 = row[2]
                a4 = row[3]
                print("="*40)
                print(a1,a2,a3,a4) 
                print("="*40)
        except sqlite3.Error as e : 
            print(e) 
        imformationpeople = input('เลือกลำดับรายชื่อของท่าน : ')
        
        conn = sqlite3.connect (r'E:\Chawadon_python\ProjectAA.db')
        c = conn.cursor()
        c.execute("""SELECT id,fname,lname,pas FROM covid WHERE id = ?""",(imformationpeople,))
        rows = c.fetchall()
        for row in rows:
            a1 = row[0]
            a2 = row[1]
            a3 = row[2]
            a4 = row[3]
        fname = row[1]
        lname = row[2]
        maa,mab,mac,mad,mae,maf,mag,mah=0,0,0,0,0,0,0,0
        sum = 0 
        pas = row[3]
        print ("กรุณากรอกข้อมูลตามความเป็นจริงของท่าน")
        scor = 0
        ps1 = input('มีไข้ สูงกว่า 37.5 องศาเซลเซียส (Y/N) : ')
        if ps1 == 'Y':
            maa = 1
        ps2 = input('มีไข้หรือไม่ (Y/N) :')
        if ps2 == 'Y':
            mab = 1
        ps3 = input('ไอแห้งหรือไม่ (Y/N) : ')
        if ps3 == 'Y':
            mac = 1
        ps4 = input('ไอมีเสมหะหรือไม่ (Y/N) : ')
        if ps4 == 'Y':
            mad = 1 
        ps5 = input('เจ็บคอหรือไม่ (Y/N) : ')
        if ps5 == 'Y':
            mae = 1 
        ps6 = input('มีน้ำมูกหรือไม่ (Y/N) : ')
        if ps6 == 'Y':
            maf = 1
        ps7 = input('ปวดกล้ามเนื้อ (Y/N) : ')
        if ps7 == 'Y':
            mag = 1
        ps8  = input('อ่อนเพลีย (Y/N) : ')               
        if ps8 == 'Y':
            mah = 1
        sum = maa+mab+mac+mad+mae+maf+mag+mah
        if sum >= 6 :
            print("="*30)
            print('| ท่านมีอากาศเสี่ยงเป็น  COVID-19  |\n| กรุณาอยู่ในพื้นที่กักตัว 14 วัน       |\n| เฝ้าระวังห้ามใช้สิ่งของร่วมกับคนอื่น   |')
            print("="*30)
        elif sum <=5:
            print("="*29)
            print('| ท่านไม่มีอากาศเสี่ยงเป็น  COVID-19 |\n| มั่นสังเกตอาการตัวเองบ่อยครั้ง |')
            print("="*29)
        elif sum <= 3:
            print("="*29)
            print('ท่านไม่มีอากาศเสี่ยงเป็น  COVID-19\nเป็นไข้หวัดปกติ')
            print("="*29)
        imformation(fname,lname,pas,ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8)

    elif choice == 'h': #แก้ไขข้อมูลผู้เสี่ยง      COVID-19
        show2()
        iid = input('เลือกลำดับที่ต้องการแก้ไข : ')
        ps1 = input('มีไข้ สูงกว่า 37.5 องศาเซลเซียส (Y/N) : ')
        ps2 = input('มีไข้หรือไม่ (Y/N) :')
        ps3 = input('ไอแห้งหรือไม่ (Y/N) : ')
        ps4 = input('ไอมีเสมหะหรือไม่ (Y/N) : ')
        ps5 = input('เจ็บคอหรือไม่ (Y/N) : ')
        ps6 = input('มีน้ำมูกหรือไม่ (Y/N) : ')
        ps7 = input('ปวดกล้ามเนื้อ (Y/N) : ')
        ps8  = input('อ่อนเพลีย (Y/N) : ')
        editimformation(ps1,ps2,ps3,ps4,ps5,ps6,ps7,ps8)  

    elif choice == 'd':
        show2()
        delete()
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
