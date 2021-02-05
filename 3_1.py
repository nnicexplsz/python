'''
print("เลือกเมนูเพื่อทำรายการ") # แบบฝึกหัด 3.1
print("##################")
print("กด 1 เพื่อเลือกเหมาจ่าย")
print("กด 2 เพื่อเลือกจ่ายเพิ่ม")
x = int(input(":"))
y = int(input("กรุณากรอกระยะทาง"))
if x==1:
    if y>=25 :
        print("ค่าใช้จ่ายทั้งหมด : 80 บาท")
    else :
        print("ค่าใช้จ่ายทั้งหมด : 25 บาท")
elif x==2:
    if y<=25 :
        print("ค่าใช้จ่ายทั้งหมด : 25 บาท")
    else:
        print("ค่าใช้จ่ายทั้งหมด : 80 บาท")
else:
    print("ทำรายการไม่ถูกต้อง")
'''
'''
value = int(input("กรุณากรอกจำนวนครั้งการรับค่า")) # แบบฝึกหัด 3.2
i = 1
a = 0 
while(i <= value) :
    number = int(input("กรอกตัวเลข :"))
    i=i+1
    a=a+number
print("ผลรวมที่รับค่ามาทั้งหมด = %d"%a)
'''
print("ป้อนชื่ออาหารโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
foodlist[]
i = 0 
while(True):
    i = i +1
    print("อาหารโปรดลำดับที่",i,end="")
    choose = input("คือ\t")
    foodlost.append(choose)
    if choose == "exit" :
        break
print("รายการอาหารสุพดโปรดของคุณ มีดังนี้",end="")
for z in range(1,i) :
    print(i,".",foodlist[z-1],end="  ")
