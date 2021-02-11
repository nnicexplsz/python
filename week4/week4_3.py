import time 
name = []
score = []
temes = []
hlt = [] 
def time_():
    timeis = time.localtime()
    a = time.strftime("%d %B %Y, %H:%M:%S", timeis)
    print(a)
num = int(input("กรุณาพิมพ์จำนวนผู้ซ้อมยิงปืน"))
for i in range (num) :
    print("ป้อมข้อมูลคนที่",1+i)
    na = input("ชื่อ :")
    sc = float(input("คะแนน :"))
    t = float(input("เวลาที่ใช้ :"))
    name.append(na)
    score.append(sc)
    temes.append(t)
    hlt.append(sc/t)
for i in range(num):
    k = i 
    for k in range(num):
        if hlt[i] > hlt[k]:
            a,b,c,d = hlt[i],name[i],score[i],temes[i]
            hlt[i],name[i],score[i],temes[i], = hlt[k],name[k],score[k],temes[k]
            hlt[k],name[k],score[k],temes[k], = a,b,c,d 
timeis = time.localtime()
a = time.strftime("%A", timeis)
b = time.strftime("%Y", timeis)
print("Shotgun"+a+"Training",b,"\nCondtion : 1")
time_()
print("-"*75)
print("{0:-<6}{1:-<6}{2:-<8}{3:-<20}{4:-<12}{5:-<15}{6}".format("NO.","PTS","TIME","COMPETITOR# Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
print("-"*75)
for i in range(num):
    stawe_po = (hlt[i]/hlt[0])*50
    stawe_pe = (stawe_po/(hlt[0]/hlt[0]*50))*100
    print("{0:<6}{1:<6}{2:<8}{3:<17}{4:<12}{5:<15}{6}".format(i+1,int(score[i]),int(temes[i]),name[i],"%.4f"%hlt[i],"%.4f"%stawe_po,"%.2f"%stawe_pe))
       