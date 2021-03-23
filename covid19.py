# import requestsr 
# response=requestsr.get("https://covid19.th-stat.com/api/open/cases/sum")
# data=response.json()


# for i,(k,v) in enumerate(data["Province"].improt()):
#     print("Name = ",k ,"Case= " ,v)



print("อาการของคุณ")
  f=input("มีไข้ สูงกว่า 37.5 องศาเซลเซียส (Y/N) :")
  if (f=='Y'):
      scor += 1

  a=input("มีอาการไข้หรือไม่ (Y/N) :")
  if (a=='Y'):
     scor += 1

  b=input("ไอแห้งหรือไม่ (Y/N) :")
  if (b=='Y'):
      scor += 1

  c=input("ไอมีเสมหะหรือไม่ (Y/N) :")
  if (c=='Y'):
      scor += 1

  d=input("เจ็บคอหรือไม่ (Y/N) :")
  if (d=='Y'):
      scor += 1

  e=input("มีน้ำมูกหรือไม่ (Y/N) :")
  if (e=='Y'):
      scor += 1

  g=input("ไอมีเสมหะหรือ (Y/N) :")
  if (g=='Y'):
      scor += 1

  h=input("ไอมีเสมหะหรือ (Y/N) :")
  if (h=='Y'):
      scor += 1

  print(scor)

   if a == 1:
    input_date()
  elif a == 2:
    
  elif a == 3:
    
  elif a == 4:


      def input_date():
  name=input("Your name: ")
  age=int(input("Your age:  "))
  pas=int(input("Your pass: "))
  sex=input("Your Male or Female: ")
  scor=0
  try:
      conn = sqlite3.connect(r'E:\Chawadon_python\test.db')
      c =conn.cursor()
      date = (name,a,p,s)
      sql = '''INSERT INTO Covid19 (Name,Age,Pass,Sex) VALUES(?,?,?,?)'''
      c.execute(sql,date) 
      conn.commit()
      c.close()
    # except sqlite3.Error as e:
    #     print('Failed to insert : ',e)
    # finally:
    #     if conn:
    #         conn.close()

# def exitt():
#     print ("ออกจากระบบ")
