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