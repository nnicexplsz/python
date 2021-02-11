t = 5 
vocadulary = {
    "rose apple":"    n.คำนาม     ชมพู่ ",
    "keyboard":"      n.คำนาม     คีย์บอร์ด",
    "drink":"         v.คำกริยา    ดื่ม ",
    "speak":"         v.คำกริยา    พูด",
    "These":"         adj.ขยายคำนาม    พวกนี้",
}
while(True):
    print("พจนานุกรม\n 1)เพิ่มคำศัพท์\n 2)แสดงคำศัพท์\n 3)ลบคำศัพท์\n 4)ออกจากโปรแกรม\n")
    data = int(input("Input Choice :"))
    if data == 1 :
        t += 1 
        terminology = input("เพิ่มคำศัพท์\t:")
        work_type = input("ชนิดของคำ (ชนิดของคำ(n.,v.,adj.,adv.) :")
        if work_type == "n.":
            work_type = "n.คำนาม"
        elif work_type == "v." :
            work_type = "v.คำกริยา"
        elif work_type == "adj." :
            work_type = "adj.ขยายคำนาม"
        elif work_type == "adv." :
            work_type = "adv.กริยาวิเศษณ์"
        meaning = input("ความหมาย\t :") 
        vocadulary[terminology] = "      "+work_type+"      "+meaning 
        print("เพิ่มคำศัพท์เรียบร้อยแล้ว")
    elif data == 2 : 
        print(15*"-"+"\n  คำศัพท์มีทั้งหมด ",t," คำ\n",15*"-")
        print("คำศัพท์      ประเภท       ความหมาย")
        for i in vocadulary :
            print (i+vocadulary[i])
    elif data == 3:
        delete = input("พิมพ์คำศัพท์ที่ต้องการลบ :")
        x = input("ต้องการลบ"+delete+"ใช่หรือไม่ (yes / no):")
        if x == "yes":
            vocadulary.pop(delete)
            t -= 1 
            print("ลบ"+delete+"เรียบร้อยแล้ว")
    else:
        yes = input("ต้องการออกจากโปรแกรมใช่หรือไม่ (yes / no):")
        if yes == "yes":
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break