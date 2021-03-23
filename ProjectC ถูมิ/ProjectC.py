from os import system, name
import datetime
subject = []
exit = 0
menu = ""
def clear():
    if name == 'nt': 
        _ = system('cls')  
    else: 
        _ = system('clear') 
def Menu(x):
    while(x=="" or x==False):
        now = datetime.datetime.now() 
        day = now.strftime("%A    %H:%M")
        date_time = now.strftime("%d/%m/%Y")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t#\t  Date/Time:\t   #")
        print("#\t\t\t\tSubject Registration System\t\t#      " + day  + "\t   #")
        print("#\t\t\t\t\t\t\t\t\t#\t " + date_time + "\t   #")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:^}{1:^98}{2:^}".format("#","[ Menu ]","#"))
        print("#\t\t\t\t\t(1) Add Subject\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(2) Delete Subject\t\t\t\t\t   #")
        print("#\t\t\t\t\t(3) Show Subject Added\t\t\t\t\t   #")
        print("#\t\t\t\t\t(4) Show Available Subject\t\t\t\t   #")
        print("#\t\t\t\t\t(5) Exit Program\t\t\t\t\t   #")
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        x = str(input("Select Menu(Ex. 1,2,3,4,5) : "))
        if(x=="1" or x=="2" or x=="3" or x=="4" or x=="5"):
            clear()
            continue
        else:
            clear()
            print("\n")
            print("{0:#^100}".format(""))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:#^100}".format(""))
            print("\n")
            x=False
    return x
def addmenu():
    while True:
        print("\n")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:^}{1:^98}{2:^}".format("#"," Add Menu ","#"))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:^}{1:^98}{2:^}".format("#","[ Menu ]","#"))
        print("#\t\t\t\t\t(1) Select the Subject\t\t\t\t\t   #")
        print("#\t\t\t\t\t(2) Back to Home Page\t\t\t\t\t   #")
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        choose = str(input("Select the option(1,2,3) : "))
        clear()
        if choose == "1":
            print("\n")
            print("{0:#^100}".format(""))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:^}{1:^98}{2:^}".format("#","Subject you can learn in our system","#"))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:#^100}".format(""))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:^}{1:^98}{2:^}".format("#"," All Course in system ","#"))
            print("#\t\t\t\t\t(1) Science\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(2) Mathematic\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(3) Thai\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(4) English\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(5) Social Studies\t\t\t\t\t   #")
            print("#\t\t\t\t\t(6) Computer\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(7) Physical Education\t\t\t\t\t   #")
            print("#\t\t\t\t\t(8) Career\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(9) Art\t\t\t\t\t\t\t   #")
            print("#\t\t\t\t\t(10) Quality of life\t\t\t\t\t   #")
            print("{0:^}{1:^95}{2:^8}".format("#","(11) Back to menu","#"))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:#^100}".format(""))
            selected = str(input("Choose subject by input number : "))
            clear()
            if selected == "1":
                if "Science" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Science" not in subject:
                    clear()
                    subject.insert(0,"Science")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tScience has been added.\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "2":
                if "Mathematic" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Mathematic" not in subject:
                    clear()
                    subject.insert(1,"Mathematic")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tMathematic has been added.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "3":
                if "Thai" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Thai" not in subject:
                    clear()
                    subject.insert(2,"Thai")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tThai has been added.\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "4":
                if "English" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "English" not in subject:
                    clear()
                    subject.insert(3,"English")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tEnglish has been added.\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "5":
                if "Social Studies" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Social Studies" not in subject:
                    clear()
                    subject.insert(4,"Social Studies")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t   Social Studies has been added.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "6":
                if "Computer" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Computer" not in subject:
                    clear()
                    subject.insert(5,"Computer")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tComputer has been added.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "7":
                if "Physical Education" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Physical Education" not in subject:
                    clear()
                    subject.insert(6,"Physical Education")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tPhysical Education has been added.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "8":
                if "Career" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Career" not in subject:
                    clear()
                    subject.insert(7,"Career")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tCareer has been added.\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "9":
                if "Art" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Art" not in subject:
                    clear()
                    subject.insert(8,"Art")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t\tArt has been added.\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "10":
                if "Quality of life" in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t    You have already added them.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                elif "Quality of life" not in subject:
                    clear()
                    subject.insert(9,"Quality of life")
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\t   Quality of life has been added.\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    addmenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            elif selected == "11":
                clear()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif choose == "2":
            clear()
            break
        else:
            clear()
            print("\n")
            print("{0:#^100}".format(""))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:#^100}".format(""))
            print("\n")
            continue 
def deletemenu():
    while True:
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:^}{1:^98}{2:^}".format("#","Subject number menu","#"))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(1) Science\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(2) Mathematic\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(3) Thai\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(4) English\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(5) Social Studies\t\t\t\t\t   #")
        print("#\t\t\t\t\t(6) Computer\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(7) Physical Education\t\t\t\t\t   #")
        print("#\t\t\t\t\t(8) Career\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(9) Art\t\t\t\t\t\t\t   #")
        print("#\t\t\t\t\t(10) Quality of life\t\t\t\t\t   #")
        print("#\t\t\t\t\t(11) DELETE ALL SUBJECTS\t\t\t\t   #")
        print("{0:^}{1:^95}{2:^8}".format("#","(12) Back to menu","#"))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:^}{1:^98}{2:^}".format("#","All Subject in your account you have registered","#"))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        for x in subject:
            print("{0:^}{1:^98}{2:^}".format("#",x,"#"))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        selected = str(input("Choose subject you want to delete : "))
        clear()
        if selected == "1":
            if "Science" in subject:
                clear()
                subject.remove("Science")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tScience has been remove from your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Science" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tYou don't have Science in your account.\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "2":
            if "Mathematic" in subject:
                clear()
                subject.remove("Mathematic")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tMathematic has been remove from your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Mathematic" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tYou don't have Mathematic in your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "3":
            if "Thai" in subject:
                clear()
                subject.remove("Thai")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tThai has been remove from your account.\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Thai" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tYou don't have Thai in your account.\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "4":
            if "English" in subject:
                clear()
                subject.remove("English")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tEnglish has been remove from your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "English" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:^}{1:^98}{2:^}".format("#","You don't have English in your account.","x"))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "5":
            if "Social Studies" in subject:
                clear()
                subject.remove("Social Studies")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tSocial Studies has been remove from your account.\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Social Studies" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:^}{1:^98}{2:^}".format("#","You don't have Social Studies in your account.","x"))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "6":
            if "Computer" in subject:
                clear()
                subject.remove("Computer")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tComputer has been remove from your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Computer" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:^}{1:^98}{2:^}".format("#","You don't have Computer in your account.","x"))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "7":
            if "Physical Education" in subject:
                clear()
                subject.remove("Physical Education")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tPhysical Education has been remove from your account.\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Physical Education" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:^}{1:^98}{2:^}".format("#","You don't have Physical Education in your account.","x"))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "8":
            if "Career" in subject:
                clear()
                subject.remove("Career")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tCareer has been remove from your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Career" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:^}{1:^98}{2:^}".format("#","You don't have Career in your account.","x"))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "9":
            if "Art" in subject:
                clear()
                subject.remove("Art")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tArt has been remove from your account.\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Art" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:^}{1:^98}{2:^}".format("#","You don't have Art in your account.","x"))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "10":
            if "Quality of life" in subject:
                clear()
                subject.remove("Quality of life")
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tQuality of life has been remove from your account.\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            elif "Quality of life" not in subject:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tYou don't have Quality of life in your account.\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                deletemenu()
                break
            else:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "11":
            try:
                if "Science" and "Mathematic" and "Thai" and "English" and "Social Studies" and "Computer" and "Physical Education" and "Art" and "Career" and "Quality of life" not in subject:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tYou don't have any subject in your account\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    deletemenu()
                    break
                elif "Science" or "Mathematic" or "Thai" or "English" or "Social Studies" or "Computer" or "Physical Education" or "Art" or "Career" or "Quality of life" in subject:
                    clear()
                    subject.clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:^}{1:^98}{2:^}".format("#","All Subjects have been remove from your account","#"))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    deletemenu()
                    break
                else:
                    clear()
                    print("\n")
                    print("{0:#^100}".format(""))
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
                    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                    print("{0:#^100}".format(""))
                    print("\n")
                    continue
            except ValueError:
                clear()
                print("\n")
                print("{0:#^100}".format(""))
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("#\t\t\t\tError ! Please check it...\t\t\t\t\t   #")
                print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
                print("{0:#^100}".format(""))
                print("\n")
                continue
        elif selected == "12":
            clear()
            break
        else:
            clear()
            print("\n")
            print("{0:#^100}".format(""))
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
            print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
            print("{0:#^100}".format(""))
            print("\n")
            continue
def Show():
    clear()
    print("\n")
    print("{0:#^100}".format(""))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("{0:^}{1:^98}{2:^}".format("#","All Subject in your accout you have registered","#"))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("{0:#^100}".format(""))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    for x in subject:
        print("{0:^}{1:^98}{2:^}".format("#",x,"#"))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("{0:#^100}".format(""))
    print("\n")
def ShowAllSubject():
    clear()
    print("\n")
    print("{0:#^100}".format(""))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("{0:^}{1:^98}{2:^}".format("#","All Subject in our system you can registered","#"))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("{0:#^100}".format(""))
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tScience\t\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tMathematic\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tThai\t\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tSocial Studie\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tEnglish\t\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tComputer\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tArt\t\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tPhysical Education\t\t\t\t\t   #")
    print("#\t\t\t\t\tCareer\t\t\t\t\t\t\t   #")
    print("#\t\t\t\t\tQuality of life\t\t\t\t\t\t   #")
    print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
    print("{0:#^100}".format(""))
    print("\n")
while(exit==0):
    menu = ""
    menu = str(Menu(menu))
    if(menu=="1"):
        clear()
        addmenu()
    elif(menu=="2"):
        clear()
        deletemenu()
    elif(menu=="3"):
        clear()
        Show()
    elif(menu=="4"):
        clear()
        ShowAllSubject()
    elif(menu=="5"):
        clear()
        break
    else :
        print("\n")
        print("{0:#^100}".format(""))
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("#\t\t\t\tError input! Please check it...\t\t\t\t\t   #")
        print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
        print("{0:#^100}".format(""))
        print("\n")
print("\n")
print("{0:#^100}".format(""))
print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
print("#\t\t\t\tThank you for use our devices....\t\t\t\t   #")
print("#\t\t\t\t\t\t\t\t\t\t\t\t   #")
print("{0:#^100}".format(""))
print("\n")