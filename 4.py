import os 
price = [50,100,200,350,1000,2000]
wallet =[60,105,225,375,1185,2370]
good = [0,0,0,0,0,0]
def product():
    print(" รายการสินค้า\n",20*"-")
    for i in range(6):
        print(i+1+"STEAM WALLET",wallet[i]," ราคา",price[i],"บาท")

def choose():
    for i in range(6):
        print(i+1+"STEAM WALLET",wallet[i],"Wallet")
    data1 = int(input("กรุณาเลือกหยิบสินค้าหมายเลข :"))
    for i in range(6):
        if data1 == i+1:
            good[i] +=1

def show():
    sumz = 0
    sumx = 0 
    print(" ___สินค้าของคุณที่หยิบมีดังนี้___\n---สินค้า",17*"-"+"จำนวน",10*"-"+"ราคา---")
    for i in range(6):
        sumz = sumz+good[i]
        sumx = sumx+(goods[i]*pricr[i])
        if good[i] > 0:
            print("STEAM WALLET",wallet[i]," Wallet",6*"-",good[i],12*"-",good[i]*price[i])
    print("รวม",23*"-",sumz,12*"-",sumx)

while(True):
    print("โปรแกรมเติม STEAM WALLET \n ",25*"-")
    print("1.แสดงรายการสินค้า \n 2.หยิบสินค้าเข้าตะกร้า \n 3.จำนวนและราคาสินค้าที่หยิบ \n 4.ปิดโปรแกรม\n")
    data = int(input("กรุณาเลือกทำรายการ :"))
    if data == 1: