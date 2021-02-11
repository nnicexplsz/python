'''
print("ป้อนชื่ออาหารโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
foodlist=[]
i = 0 
while(True):
    i = i +1
    print("อาหารโปรดลำดับที่",i,end="")
    choose = input("คือ\t")
    foodlist.append(choose)
    if choose == "exit" :
        break
print("รายการอาหารสุพดโปรดของคุณ มีดังนี้",end="")
for z in range(1,i) :
    print(z,".",foodlist[z-1],end="  ")
'''
'''
a = []
while True:
    b = input("ร้านวันไหนว่าง\n เพิ่ม [a] \n แสดง [s]\n ออกจากระบบ [x]\n")
    b = b.lower()
    if b=="a" :
        c = input("ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)")
        a.append(c)
        print("\n*******ข้อมูลได้เข้าสู่ระบบแล้ว******")
    elif b=="s" :
        print("{0:-<6}{0:-<10}{0:-<10A}".format(""))
        print("{0:-<8}{1:-<10}{2:-<10}".format("รหัส","ชื่อ","จังหวัด"))
        print("{0:-<6}{0:-<10}{0:-<10}".format(""))
        for d in a :
            e = d.split(":")
            print("{0[0]:<6 {0[1]:<10} ({0[2]:<10})".format(e))
            continue
    elif b == "x":
        break
print("ทำคำสั่งต่อไป")
'''
'''

student = int(input("จำนวนนักเรียน:"))
print("-"*20)
point_grade = [0,0,0,0,0,0]
score_grade = [" 90-100:"," 80-89 :"," 70-79 :"," 60-69 :"," 50-59 :","  0-49 :"]
x = 1 
while x <= student :
    point = int(input("จำนวนคะแนนนักเรียน :"))
    if point <= 100 and point >= 90 :
        point_grade[0] += 1 
    elif point < 90 and point >= 80 :
        point_grade[1] += 1 
    elif point < 80 and point >= 70 :
        point_grade[2] += 1
    elif point < 70 and point >= 60 :
        point_grade[3] += 1
    elif point < 60 and point >= 50 :
        point_grade[4] += 1
    elif point < 50 and point >= 0 :
        point_grade[5] += 1 
        x = x+1 
for x in range(0,6) :
    print(score_grade[x],"*"*point_grade[x])
'''

student = int(input('กรุณากรอกจำนวนนักเรียน :'))
print('-'*30)
total = [0 , 0 , 0 , 0 , 0 , 0]
score = ['90-100 :','80-89 :','70-79 :','60-69 :','50-59 : ','0-49 :']
x = 1
while x <= student :
    point = int(input('กรุณากรอกคะแนนนักเรียน :'))
    if point <= 100 and point >= 90 :
        total[0] += 1
    elif point < 90 and point >= 80 :
        total[1] += 1
    elif point < 80 and point >= 70 :
        total[2] += 1
    elif point < 70 and point >= 60 :
        total[3] += 1
    elif point < 60 and point >= 50 :
        total[4] += 1
    elif point < 50 and point >= 0 :
        total[5] +=1
    x = x+1
for x in range(0,6) :
    print(score[x],'*'*total[x])