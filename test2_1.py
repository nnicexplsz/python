'''
x = input("Input Your First Number : ")
y = input("Input Youur Second Number : ")
print("%s = "%x,"%s"%y, ":",x==y)
print("%s > "%x,"%s"%y, ":",x>y)
print("%s < "%x,"%s"%y, ":",x<y)
'''


'''
print('Day Converter Program')
day = input('Input number of Days --> ')
print('%s'%day,'Days --> Hour',int(day)*24,'Hour')
print('%s'%day,'Days --> Minutes',int(day)*24*60,'Minutes')
print('%s'%day,'Days --> Seconds',int(day)*24*60*60,'Seconds')
'''

'''
friend = [ 'jan','cream','phu','bam','orm','pee','bas','kong','da','james' ]
friend.append("dom")
friend.append("poondang")
friend.insert(1,"csa")
friend.insert(8,"ped")
friend.pop(3)
del friend[7]
friend.clear()
print(friend) 
'''

#โปรแกรมหยิบสินค้าใส่ตระกร้า
a = input("หยิบสินค้าครั้งที่ 1 :")
b = input("หยิบสินค้าครั้งที่ 2 :")
c = input("หยิบสินค้าครั้งที่ 3 :")
d = input("หยิบสินค้าครั้งที่ 4 :")
e = input("หยิบสินค้าครั้งที่ 5 :")
basket = []
basket.append(a)
basket.append(b)
basket.append(c)
basket.append(d)
basket.append(e)
print('1.',basket[0])
print('2.',basket[1])
print('3.',basket[2])
print('4.',basket[3])
print('5.',basket[4])

'''
print("โปรแกรมคำนวณค่าผ่านทางสอเตอร์เวย์")
print("-----------------------------")
print("รถยนต์ 4 ล้อ               กด 1")
print("รถยนต์ 6 ล้อ               กด 2")
print("รถยนต์มากกว่า 6 ล้อ         กด 3")

car = input("เลือกประเภทยานยนต์")
if a==1:
    print("ค่าบริการรถยนต์ 4 ล้อ")
    print("")


thisdict1 = {
    "ลาดกระบัง บางบ่อ" : "25" 
    "ลาดกระบัง บางประกง" : "30" 
    "ลาดกระบัง พนัสนิคม" : "40" 
    "ลาดกระบัง บ้านบึง" : "55" 
    "ลาดกระบัง บางพระ" : "60" 
}
print(thisdict4) 
'''

car4 = {
    'ลาดกระบัง-บางบ่อ' : '30 บาท',
    'ลาดกระบัง-บางปะกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '55 บาท',
    'ลาดกระบัง-บ้านบึง' : '60 บาท',
    'ลาดกระบัง-บางพระ' : '80 บาท'
}

car6 = {
    'ลาดกระบัง-บางบ่อ' : '45 บาท',
    'ลาดกระบัง-บางปะกง' : '45 บาท',
    'ลาดกระบัง-พนัสนิคม' : '75 บาท',
    'ลาดกระบัง-บ้านบึง' : '90 บาท',
    'ลาดกระบัง-บางพระ' : '100 บาท'
}

cars6 = {
    'ลาดกระบัง-บางบ่อ' : '60 บาท',
    'ลาดกระบัง-บางปะกง' : '70 บาท',
    'ลาดกระบัง-พนัสนิคม' : '110 บาท',
    'ลาดกระบัง-บ้านบึง' : '130 บาท',
    'ลาดกระบัง-บางพระ' : '140 บาท'
}

print('โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('รถยนต์ 4 ล้อ กด 1')
print('รถยนต์ 6 ล้อ กด 2') 
print('รถยนต์มากกว่า 6 ล้อ กด 3')

a=int(input('เลือกประเภทพาหนะ :'))
if a==1:
    print('ค่าบริการรถยนต์ 4 ล้อ')
    print(*car4.items(), sep='\n')
if a==2:
    print('ค่าบริการรถยนต์ 6 ล้อ')
    print(*car6.items(), sep='\n')
if a==3:
    print('ค่าบริการรถยนต์มากกว่า 6 ล้อ')
    print(*cars6.items(), sep='\n')

print('โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('รถยนต์ 4 ล้อ กด 1')
print('รถยนต์ 6 ล้อ กด 2') 
print('รถยนต์มากกว่า 6 ล้อ กด 3')

a=int(input('เลือกประเภทพาหนะ :'))
if a==1:
    print('ค่าบริการรถยนต์ 4 ล้อ')
    print(*car4.items(), sep='\n')
if a==2:
    print('ค่าบริการรถยนต์ 6 ล้อ')
    print(*car6.items(), sep='\n')
if a==3:

    
    print('ค่าบริการรถยนต์มากกว่า 6 ล้อ')
    print(*cars6.items(), sep='\n')
    print('โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์')
print('รถยนต์ 4 ล้อ กด 1')
print('รถยนต์ 6 ล้อ กด 2') 
print('รถยนต์มากกว่า 6 ล้อ กด 3')

a=int(input('เลือกประเภทพาหนะ :'))
if a==1:
    print('ค่าบริการรถยนต์ 4 ล้อ')
    print(*car4.items(), sep='\n')
if a==2:
    print('ค่าบริการรถยนต์ 6 ล้อ')
    print(*car6.items(), sep='\n')
if a==3:
    print('ค่าบริการรถยนต์มากกว่า 6 ล้อ')
    print(*cars6.items(), sep='\n')
    