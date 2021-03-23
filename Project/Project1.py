import sqlite3
conn = sqlite3.connect("Project1.db")
c = conn.cursor()
# c.execute('''CREATE TABLE gun (id integer PRIMARY KEY AUTOINCREMENT,
#     Name varchar(30) NOT NULL,
#     Level varchar(30) NOT NULL,
#     Groupp varchar(2) NOT NULL,
#     Field1 float NOT NULL,
#     Field2 float NOT NULL,
#     Field3 float NOT NULL,
#     Field4 float NOT NULL,
#     Field5 float NOT NULL,
#     Field6 float NOT NULL,
#     Field7 float NOT NULL,
#     Field8 float NOT NULL,
#     Field9 float NOT NULL,
#     Field10 float NOT NULL,
#     Scoresum varchar(30) NOT NULL,
#     Typell varchar(30) NOT NULL)''')
conn.commit()
conn.close()
category = ["Open","Standard","Modify","Standard manual"]
m = " U" 
ma = "0"




def input_date():
    print('กรุณากรอกข้อมูลดั้งต่อไปปนี้')
    name = input('กรอกชื่อและนามสกุลของท่าน :')
    print('ประเภทของการแข่งขันมีดังนี้\n1.Open คือ ปืนลูกซองแบบแมกกาซีน\n2.Standard คือ ปืนออนโต้แบบไม่ได้แต่งปืน\n3.Modify คือ ปืนออโต้แบบติดดอท ใส่คอมพ์ลดแรงรีคอย\n4.Standard manual คือ ปืนลูกซองแบบปั้มไม่แต่งอะไร')
    p = int(input('กรุณาเลือกประเภทของท่าน :'))
    co = category[p+1]
    co = "man"
    s = input('กรุณาเลือกลำดับกลุ่มของท่าน(1-5):')
    try:
        conn = sqlite3.connect(r"E:\Chawadon_python\Project\Project1.db")
        c =conn.cursor()
        date = (name,m,s,0,0,0,0,0,0,0,0,0,0,ma,co)
        sql = '''INSERT INTO gun (Name,Level,Groupp,Field1,Field2,Field3,Field4,Field5,Field6,Field7,Field8,Field9,Field10,Scoresum,Typell) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        c.execute(sql,date) 
        conn.commit()
        c.close()
    except sqlite3.Error as e:
        print('Failed to insert : ',e)
    finally:
        if conn:
            conn.close()

def show():
    print('กรุณาเลือกดูข้อมูล\nดูทั้งหมดกด[1]\nเฉพาะข้อมูลของท่านกด[2]')
    information = int(input('กรุณาเลือกหมายเลขของท่าน :'))
    if information == 1:
        c = conn.cursor()
        c.execute('''SELECT * FROM gun''')
        result = c.fetchall()
        print("{0:-<30}{1:-<20}{2:-<10}{3:-<20}{4:-<7}{5:-<7}{6:-<7}{7:-<7}{8:-<7}{9:-<7}{10:-<7}{11:-<7}{12:-<7}{13:-<7}{14:-<10}".format("ชื่อ-นามสกุล","ประเภทที่เล่น","เลเวล","กลุ่มที่อยู่","รอบ1","รอบ2","รอบ3","รอบ4","รอบ5","รอบ6","รอบ7","รอบ8","รอบ9","รอบ10","คะแนนรวม"))
        for x in result:
            if x[3] != 0:
                print("{0: <30}{1: <20}{2: <10}{3: <20}{4: <7}{5: <7}{6: <7}{7: <7}{8: <7}{9: <7}{10: <7}{11: <7}{12: <7}{13: <7}{14: <10}".format(x[0],x[14],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13]))
            else:
                print("{0: <30}{1: <20}{2: <10}{3: <20} ยังไม่มีการกรอกคะแนน!".format(x[0],x[14],x[1],x[2]))
            
                

        name = input("พิมพ์ชื่อและนามสกุลที่คุณต้องการค้นหา: ")
        name_o = (name)
        c = conn.cursor()
        c.execute(' SELECT * FROM gun WHERE Name = ?',(name_o,))
        if c.fetchone():
            c.execute(' SELECT * FROM gun WHERE Name = ?',(name_o,))
            result = c.fetchall()
            print(x)
            for x in result:
                print("ชื่อ-นามสกุล: "+str(x[0])+"\nประเภทที่เล่น: "+str(x[14])+"\nเลเวล: "+str(x[1])+"\nกลุ่มที่:"+str(x[2])+"\nคะแนนทั้ง10รอบ\n{0:-<7}{1:-<7}{2:-<7}{3:-<7}{4:-<7}{5:-<7}{6:-<7}{7:-<7}{8:-<7}{9:-<7}{10}".format("รอบ1","รอบ2","รอบ3","รอบ4","รอบ5","รอบ6","รอบ7","รอบ8","รอบ9","รอบ10","คะแนนรวม"))
                x = str(x)
                if x[3]!=0:
                    print("{0:-<7}{1:-<7}{2:-<7}{3:-<7}{4:-<7}{5:-<7}{6:-<7}{7:-<7}{8:-<7}{9:-<7}{10}".format(str(x[3]),str(x[4]),str(x[5]),str(x[6]),str(x[7]),str(x[8]),str(x[9]),str(x[10]),str(x[11]),str(x[12]),str(x[13])))
                else:
                    print("ยังไม่ลงไม่มีคะแนน!")
        else:
            print("ไม่พบชื่อของคุณ")

def points():
    around1 = []
    print("กรุณากรอกข้อมูลดังต่อไปนี้ ")
    name3 = input("พิมพ์ชื่อของคุณ :")
    data1 = (name3,)
    c = conn.cursor() 
    c.execute("""SELECT * FROM gum WHERE Name = ?""",data1)
    if c.fetchone():
        print("กรอกคะแนนในแต่ละรอบ ") 
        for xy in range(10):
            around_a = float( input ("คะแนนรอบที่ :"+ str (xy+1)))
            around1.append(around_a)
        
        
    else :
        print("ยังไม่มีชื่อคุณ")


def exitt():
    print ("ออกจากระบบ")
print('ยินดีต้อนรับเข้าสู่โปรแกรมยิงปืน\nกรุณาเลือกรายการดั้งต่อไปนี้\nกด[1].ลงทะเบียน\nกด[2].ดูข้อมูลของท่าน\nกด[3].กรอกคะแนนการแข่งขัน\nกด[4].ออกจากระบบ')
a = int(input('กรุณากรอกตัวเลือกของท่าน :'))
if a == 1:
    input_date()
elif a == 2:
    show()
elif a == 3:
    points()
elif a == 4:
    exitt()

