def password():
    from getpass import getpass
    key=getpass("Enter password:")
    if key=='deep91':
        print ("Welcome")
    else:
        print("Access Denied!!")
def insert_rec():
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd='@6107',database='practice')
    if mydb.is_connected:
        print("Connection successfully established")
    else:
        print("Connection cannot be established")
    mycursor=mydb.cursor()
    mycursor.execute("create table IF NOT EXISTS student(addNo int primary key,stud_name varchar(25),f_name varchar(30),phNo varchar(20),adh_no varchar(20),dob date)")
    rec=[]
    while True:
        addNo=int(input("Enter Addmission number: "))
        stud_name=input("Enter Student name: ")
        f_name=input("Enter Father's name: ")
        phNo=input("Enter Phone number: ")
        #…
        addNo=int(input("Enter the Addmission number you want to search for: "))
        mycursor.execute("select *from student")
        row1=mycursor.fetchall()
        f=0
    for rec in row1:
        if rec[0]==addNo:
            print(rec)
            f=1
            break
    if f==0:
        print("No records found....")
def update_rec():
 # Updating records :update book details entered by user
    import mysql.connector as c
    mydb=c.connect(host="localhost",user="root",passwd='@6107',database='practice')
    if mydb.is_connected:
        print("Connection successfully established")
    else:
        print("Connection cannot be established")
        mycursor=mydb.cursor()
        f=0
    addNo=int(input("Enter the addmission number you want to update: "))
    print("Press 1 for Updating Student name")
    print("Press 2 for Updating Father name")
    print("Press 3 for Updating date of birth")
    dob=input("Enter date of purchase in yyyy-mm-dd format only: ")
    sql="update student set dob=%s where addNo=%s "
    mycursor.execute(sql,[dob,addNo])
 
 
    mydb.commit()
    print("UPDATION DONE SUCCESSFULLY....")
 
def delete_rec():
 # Deleting records entered by user
 import mysql.connector as c
 mydb=c.connect(host="localhost",user="root",passwd='@6107',database='practice')
 if mydb.is_connected:
    print("Connection successfully established")
 else:
    print("Connection cannot be established")
 mycursor=mydb.cursor()
 addNo=int(input("Enter the addmission number you want to delete: "))
 mycursor.execute("select *from student")
 row1=mycursor.fetchall()
 f=0
 for rec in row1:
    if rec[0]==addNo:
        ch=input("Do you want to delete the details???? Y/N: ")
        if ch in "Yy":
            continue
#___MAIN PROGRAMME_____
password()
print("**** STUDENT ADMIN MENU ****")
while True:
 print("*****MAIN MENU*****")
 print("Press 1 to Enter student details ")
 print("Press 2 to Search student details ")
 print("Press 3 to Update student record ")
 print("Press 4 to Delete student records ")
 print("Press 5 to Display all student records ")
 print("Press -1 to exit")
 ch=int(input("Enter your choice: "))
 if ch==1:
    insert_rec()
 elif ch==2:
    search_rec()
 elif ch==3:
    update_rec()
 elif ch==4:
    delete_rec()
 elif ch==5:
    display_rec()
 elif ch==-1:
    break
 else:
    print("You have entered a wrong choice. ")
    print("Read the menu carefully and enter your choice again.")
    continue