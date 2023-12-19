from .assets import *
from rich import print as rprint
from rich.table import Table
from time import sleep

# Def5:CLASS MAIN MENU
def Class(cursor,connection,console):
    while True:

        Enter()
        table = Table(title="Class")
        table.add_column("S. No.", style="cyan", no_wrap=True)
        table.add_column("Section", style="magenta")
        table.add_row("1","Add a Class")
        table.add_row("2","Display all classes")
        table.add_row("3","Edit the Class")
        table.add_row("4","Remove a Class")
        table.add_row("5","Go Back (Main Menu)")
        console.print(table)
        sectionValue = Choice("Enter a Choice(1,2,3,4,5)", [1, 2, 3, 4, 5])

        if sectionValue == 1:
            AddClass(cursor,connection,console)
        elif sectionValue == 2:
            DisplayClass(cursor)
        elif sectionValue == 3:
            EditClass(cursor,connection)
        elif sectionValue == 4:
            RemoveClass(cursor,connection)
        else:
            break

def AddClass(cursor,connection,console):

    numberOfClasses = Checker("Enter the Number of Classes to Add:", "int")

    for i in range(numberOfClasses):

        rprint("\n[bold violet]ENTER THE DETAILS OF THE CLASS\n")

        cursor.execute("select * from Class")
        allClasses = cursor.fetchall()
        defaultCLassID = len(allClasses) + 1


        rprint("\nDefault Class ID:", defaultCLassID)

        classNum = Checker("Enter the Class(Max 2 Digits):", "int")

        rprint("\nEnter the Division(Max 3 Characters)")
        classDiv = input(":")
        rprint("\ntEnter the Class Teacher(Max 20 Characters)")
        classTeacher = input(":")
        classNumStudents = Checker("Enter the Number Of Students(Max 3 Digits):", "int")
        rprint("\nEnter Subject 1(Max 20 Characters)")
        classSubject1 = input(":")
        rprint("\nEnter Subject 2(Max 20 Characters)")
        classSubject2 = input(":")
        rprint("\nEnter Subject 3(Max 20 Characters)")
        classSubject3 = input(":")
        rprint("\nEnter Subject 4(Max 20 Characters)")
        classSubject4 = input(":")
        rprint("\nEnter Subject 5(Max 20 Characters)")
        classSubject5 = input(":")
        
        try:
            cursor.execute(
                "insert into Class values({},{},'{}','{}',{},'{}','{}','{}','{}','{}')".format(defaultCLassID, classNum, classDiv, classTeacher, classNumStudents, classSubject1, classSubject2, classSubject3, classSubject4, classSubject5))
            connection.commit()

            Enter()
            with console.status("[bold green]Adding Details to Database...") as status:
                sleep(2)
                console.log(f'[bold][green]Class Created Added Successfully.. ')
            Enter()
            Lag()
            Enter()

        except:

            Enter()
            rprint("[bold red]ERROR : Invalid Details Entered.")
            Enter()

            wish = Choice("Do You Wish To Retry Or Go Back(Main Menu)  (1/2):", [1, 2])
            if wish == 1:
                AddClass(cursor,connection,console)
            if wish == 2:
                return 0


# Def15:DISPLAY CLASS MENU
def DisplayClass(mycursor):
    def c1():
        mycursor.execute("select * from Class")
        Enter()
        print("\t\t\t DISPLAY ALL CLASSES")
        print("-" * 90)
        print("Class ID Class\tDivision Class Tr No Of Students  Sub 1  Sub 2  Sub 3  Sub 4     Sub 5")
        print("-" * 90)
        for i in mycursor:
            print(i[0], "\t", i[1], "\t", i[2], "\t", i[3], "\t\t", i[4], "\t ", i[5], "\t", i[6], "\t", i[7], "  ",
                  i[8], "\t", i[9])
            print("-" * 90)
        Enter()
        Lag()
        Enter()

    def c2():
        mycursor.execute("select class,division,class_teacher from Class")
        Enter()
        print("\t\t\t CLASS WITH CLASS TEACHER")
        print("-" * 30)
        print("Class\tDivision Class Teacher")
        print("-" * 30)
        for i in mycursor:
            print(i[0], "\t", i[1], "\t", i[2])
            print("-" * 30)
        Enter()
        Lag()
        Enter()

    def c3():
        mycursor.execute("select class,division,no_of_students from Class")
        Enter()
        print("\t\t\t CLASS WITH NUMBER OF STUDENTS")
        print("-" * 32)
        print("Class\tDivision No Of Students")
        print("-" * 32)
        for i in mycursor:
            print(i[0], "\t", i[1], "\t", i[2])
            print("-" * 32)
        Enter()
        Lag()
        Enter()

    while True:
        Enter()
        Star()
        Enter()
        print("\t\t\t DISPLAY CLASSES")
        print("\t\t\t ***************")
        Enter()
        print("\t\t 1.DISPLAY ALL CLASSES")
        print("\t\t 2.DISPLAY CLASS WITH CLASS TEACHER")
        print("\t\t 3.DISPLAY CLASS WITH NUMBER OF STUDENTS")
        print("\t\t 4.BACK")
        Enter()
        c = Choice("\tEnter a Choice(1,2,3,4)", [1, 2, 3, 4])
        if c == 1:
            c1()
        elif c == 2:
            c2()
        elif c == 3:
            c3()
        else:
            break


# Def16:EDIT CLASS MENU
def EditClass(mycursor,lib):
    Enter()
    Enter()
    mycursor.execute("select * from Class")
    print("\t\t", "-" * 13)
    print("\t\tClass ID:")
    print("\t\t", "-" * 13)
    for i in mycursor:
        print("\t\t", i[0])
    print("\t\t", "-" * 13)
    Enter()
    p = int(input("Enter the Class ID:"))
    Enter()
    eh = []
    mycursor.execute("select * from Class")
    for i in mycursor:
        eh.append(i[0])
    if p in eh:
        EditClass2(p,mycursor,lib)
    else:
        print("Enter A Valid Class ID:")
        EditClass()


# Def16.1:EDIT CLASS MENU 2
def EditClass2(p,mycursor,lib):
    Enter()
    Star()
    Enter()
    print("\t\tWhat Do You Want to Edit")
    Enter()
    print("\t 1.Class")
    print("\t 2.Division")
    print("\t 3.Class Teacher")
    print("\t 4.No: of Students")
    print("\t 5.Subject 1")
    print("\t 6.Subject 2")
    print("\t 7.Subject 3")
    print("\t 8.Subject 4")
    print("\t 9.Subject 5")
    print("\t 10.Exit")
    Enter()
    v = Choice("Enter Your Choice(1,2,3,4,5,6,7,8,9,10):", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    if v == 1:
        Enter()
        d = Checker("\tEnter the Class (Max 2 Digits):", "int")
        try:
            mycursor.execute("update  Class set class={}  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tClass Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()

    if v == 2:
        Enter()
        d = input("\tEnter the Division(Max 3 Characters):")
        try:
            mycursor.execute("update  Class set division='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tDivision Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 3:
        Enter()
        d = input("\tEnter the Class Teacher(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set class_teacher='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tClass Teacher Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 4:
        Enter()
        d = Checker("\tEnter the No: of Students(Max 3 Digits):", "int")
        try:
            mycursor.execute("update  Class set no_of_students={}  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tNo: of students Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 5:
        Enter()
        d = input("\tEnter the Subject 1(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject1='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 1 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 6:
        Enter()
        d = input("\tEnter the Subject 2(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject2='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 2 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 7:
        Enter()
        d = input("\tEnter the Subject 3(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject3='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 3 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 8:
        Enter()
        d = input("\tEnter the Subject 4(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject4='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 4 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 9:
        Enter()
        d = input("\tEnter the Subject 5(Max 20 Characters):")
        try:
            mycursor.execute("update  Class set subject5='{}'  where class_id={}".format(d, p))
            lib.commit()
            Enter()
            print("\tSubject 5 Updated")
            Enter()
            Lag()
            Enter()
        except:
            print("Enter The Values As Per Instructions")
            Enter()
            Lag()
            Enter()
    if v == 10:
        Class()


# Def17:REMOVE CLASS MENU
def RemoveClass(mycursor,lib):
    Enter()
    g = Checker("\tEnter the Class ID:", "int")
    lk = []
    mycursor.execute("select class_id from Class")
    for i in mycursor:
        lk.append(i[0])
    if g in lk:
        try:
            mycursor.execute("delete from Class where class_id={}".format(g))
            lib.commit()
            Enter()
            print("Class With Class ID", g, "is Deleted")
            Enter()
            Lag()
            Enter()
        except:
            Enter()
            print("Cannot Delete The Class As It Is Used In Other Tables")
            Enter()
            print("Delete All The Records Which Use ", g, " As Class ID From Other Tables")
            Enter()
            Lag()
            Enter()
    else:
        Enter()
        print("Enter A Valid Class ID")
        Enter()
        Lag()
        Enter()