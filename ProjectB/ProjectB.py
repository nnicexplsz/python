


#from CSVFile import *
form = list() ; P = print
print("\n---------------------------------")
print("-------------จัดทำโดย-------------")
print("นายชวดล บรรจง 633050129-1 ")
print("นายเมธี  ศรีสมดี 633050136-4 ")
print("")
print("นักศึกษาชั้นปีที่ 1 สาขาคอมพิวเตอร์ศึกษา")
print("คณะศึกษาศาสตร์ มหาวิทยาลัยขอนแก่น")
print("---------------------------------")

def MainMenu():
    while True :
        
        P("\n-------------------------\n1.เพิ่มรายชื่อ\n2.เพิ่มน้ำหนักและส่วนสูง\n3.แสดงรายชื่อทั้งหมด\n")
        select = int(input("เลือก: "))
        if select == 1: 
            member = int(input("\nจำนวนนักศึกษาที่เพิ่ม: "))
            P("--- ระบุจำนวนนักศึกษา เรียบร้อย ---")
            P("\nกรุณาระบุ รหัสประจำตัวนักศึกษา และชื่อ-สกุล")
            P("------------ ตัวอย่าง ------------")
            P(" 633050132-2 :นายอังกรู แก้ววันนา \n")
            for k in range(1,member+1) :
                idcode,name = str(input("ลำดับที่ %d : " %k)).split(':')
                form.append([str(Lencsv()),idcode,name])
                writecsv(Lencsv(),idcode,name)
            MainMenu()
        elif select == 2:
            for _F in range(int(input("เพิ่มกี่ครั้ง: "))):
                idx = int(input("ลำดับที่: "))
                H = eval(input("ส่วนสูง: "))
                W = eval(input("น้ำหนัก: "))
                addrow(idx, W, H)
            MainMenu()
        elif select == 3:
            for G in readcsv():
                P(G.replace(","," ")[:-1])
            MainMenu()
        elif select == 0: exit(0)
        else: MainMenu()

def writecsv(no,id,name):
   Data = open("d:\\Dew_python\\project1\\studentlist2.csv","a",encoding='UTF8')
   Data.write("%5d, %20s, %29s\n"% (no,id,name))
   Data.close()

def readcsv():
    Data = open("d:\\Dew_python\\project1\\studentlist2.csv","r",encoding='UTF8')
    DataLine = Data.readlines()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    Data.close()
    return  DataLine

def Lencsv():
    Data = open("d:\\Dew_python\\project1\\studentlist2.csv","r",encoding='UTF8')
    DataLen = len(Data.readlines())
    Data.close()
    return DataLen

def FindBMI(weight,high):
    BMI = round(weight/(high/100)**2,2)
    if BMI<=18.5:
        return "%10s, %20s"%(BMI,"น้ำหนักน้อย / ผอม")
    elif 18.5<BMI<=23:
        return "%10s, %20s"%(BMI,"ปกติ (สุขภาพดี)")
    elif 23<BMI<=25:
        return "%10s, %20s"%(BMI,"ท้วม / โรคอ้วนระดับ 1")
    elif 25<BMI<=30:
        return "%10s, %20s"%(BMI,"อ้วน / โรคอ้วนระดับ 2")
    elif BMI>30:
        return "%10s, %20s"%(BMI,"อ้วนมาก / โรคอ้วนระดับ 3")
    else: return "%10s, %20s"%(BMI,"Input Error!")

def addrow(index,weight,high):
    Data = open("d:\\Dew_python\\project1\\studentlist2.csv","r",encoding='UTF8')
    New = Data.read().split("\n")
    NewBMI = FindBMI(weight,high)
    New[index] = New[index] + ", %10s, %10s, %s"% (high,weight,NewBMI)
    renew = "\n".join(New)
    Wirte = open("d:\\Dew_python\\project1\\studentlist2.csv","w",encoding='UTF8')
    Wirte.write(renew)

MainMenu() 