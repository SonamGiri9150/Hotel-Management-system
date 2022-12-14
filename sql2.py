def inpt():
    import random
    k=random.randint(1,100)
    if k not in R:
        R.append(k)
    l.append(k)
    u=random.randint(1,100)
    if u not in J:
        J.append(u)
    l.append(u)
    try:
        m=input("Enter your name ")
        l.append(m)
        b=input("Enter your address ")
        l.append(b)
        c=int(input("Enter your mobile number "))
        l.append(c)
        d=input("Enter check in date[format=year/month/date] " )
        l.append(d)
        e=input("Enter check out date[format=year/month/date] " )
        l.append(e)
        f=int(input("Enter the number of people staying "))
        l.append(f)
        g=input("Enter the type of room you would like to choose ")
        l.append(g)
        n=int(input("Enter the number of days of stay at the hotel "))
        cost=0
        if(g=='standard'or g=='STANDARD'):
            cost=cost+2000
            cost=cost*n
            print("You have chose a STANDARD room.You will be charged Rs.1500 per night.")
            print("The total fee to be paid is",cost)
        elif(g=='double'or g=='DOUBLE'):
            cost=cost+3500
            cost=cost*n
            print("You have chosen for a DOUBLE room.You will be charged Rs.3500 per night.")
            print("The total fee to be paid is",cost)
        elif(g=='deluxe'or g=='DELUXE'):
            cost=cost+5000
            cost=cost*n
            print("You have chosen for a DELUXE room.You will be charged Rs.5000 per night.")
            print("The total fee to be paid is",cost)
        else:
            print("Check your entry!")
            return()
        print()
        e=input("Do you wish to proceed with payment?(y/n) ")
        if(e=='y'or e=='yes'):
            print("Transaction done!")
            print()
        elif(e=='n'):
            print("No problem you are always welcome! ")
            return()
        l.append('BOOKED')
     
        o='insert into booked values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        c1.execute(o,l)
        d1.commit()
        W="select * from booked where REG_NO='%s'"
        Z=k
        c1.execute(W,(Z,))
        A=c1.fetchall()
        print()
        print("Please check your records.KEEP YOUR REGISTRATION NUMBER SAFELY FOR ALL FUTURE PURPOSES!! ")
        print(tabulate(A,headers=['REG.NO','ROOM NO.','NAME','ADDRESS','PHONE NO.','CHECK-IN','CHECK-OUT','NO.OF PEOPLE',
                                      'ROOM TYPE','STATUS'],tablefmt='psql'))
    except:
        print("Please check your data ")
        return()
def modf():
    def rep():
        k=(b,c)
        c1.execute(j,k)
        d1.commit()
    print('''1.NAME
2.ADDRESS
3.PHONE NO
4.NO.OF PEOPLE
5.ROOM TYPE''')
    def dis():
        W="select * from booked where REG_NO='%s'"
        Z=c
        c1.execute(W,(c,))
        P=c1.fetchall()
        print()
        print("Please check your new records.")
        print(tabulate(P,headers=['REG.NO','ROOM NO.','NAME','ADDRESS','PHONE NO.','CHECK-IN','CHECK-OUT','NO.OF PEOPLE',
                                  'ROOM TYPE','STATUS'],tablefmt='psql'))
    o=int(input("Enter the serial umber corrsponding to the the modification "))                                  
    if(o==1):
        b=input("Enter the new value ")
        c=int(input("Enter the reg no " ))
        j="update booked set NAME=%s where REG_NO=%s"
        rep()
        dis()
        print("The data has been modified successfuly")
    elif(o==2):
        b=input("Enter the new value ")
        c=int(input("Enter the reg no " ))
        print("Enter the correct value")
        j="update booked set ADDRESS=%s where REG_NO=%s"
        rep()
        dis()
        print("The data has been modified successfuly")
    elif(o==3):
        b=input("Enter the new value ")
        c=int(input("Enter the reg no "))
        print("Enter the correct value")
        j='update booked set PHONE_NO=%s where REG_NO=%s'
        rep()
        dis()
        print("The data has been modified successfuly")
    elif(o==4):
        b=input("Enter the new value ")
        c=int(input("Enter the reg no " ))
        print("Enter the correct value")
        j='update booked set NO_OF_PEOPLE=%s where REG_NO=%s'
        rep()
        dis()
        print("The data has been modified successfuly")
    elif(o==5):
        b=input("Enter the new value ")
        c=int(input("Enter the reg no " ))
        print("Enter the correct value")
        j='update booked set ROOMTYPE=%s where REG_NO=%s'
        rep()
        dis()
        print("The data has been modified successfuly")
def ckin():
    print("HELLO,so you are here ")
    r=int(input("Enter the registration number "))
    q='CHECKED IN'
    t=(q,r)
    s="update booked set STATUS=%s WHERE REG_NO=%s"
    c1.execute(s,t)
    d1.commit()
    print("You have successfuly checked in")
def ckout():
    print("I hope your stay at our hotel was nice!! ")
    m="UPDATE booked SET STATUS=%s where REG_NO='%s'"
    n=int(input("Please enter your registration number "))
    q='CHECKED OUT'
    t=(q,n)
    c1.execute(m,t)
    d1.commit()
    print("You have successfuly checked out!")
def adm():
    p=input("Please enter the password ")
    if(p=="star@admn"):
        print("Welcome !!")
        print('''Select your choice
1.CHECK FOR BOOKINGS
2.CHECK FOR CHECKED IN ROOMS
3.CHECK FOR CHECKED OUT ROOMS
4.CHECK FOR ALL RECORDS''')
        y=int(input("I choose "))
        if(y==1):
            c1.execute("Select REG_NO,NAME,ADDRESS,CHECK_IN,CHECK_OUT from booked where STATUS='BOOKED'")
            g=c1.fetchall()
            print(tabulate(g,headers=['REG.NO.','NAME','ADDRESS','CHECK-IN','CHECK OUT'],tablefmt='psql'))
        elif(y==2):
            c1.execute("select REG_NO,NAME,ADDRESS,PHONE_NO,CHECK_OUT,ROOMTYPE from booked WHERE STATUS='CHECKED IN'")
            g=c1.fetchall()
            print(tabulate(g,headers=['REG.NO.','NAME','ADDRESS','PHONE_NO','CHECK-OUT','ROOM TYPE'],tablefmt='psql'))
        elif(y==3):
            c1.execute("select REG_NO,NAME,ADDRESS,PHONE_NO,CHECK_IN,ROOMTYPE from booked WHERE STATUS='CHECKED OUT'")
            g=c1.fetchall()
            print(tabulate(g,headers=['REG.NO.','NAME','ADDRESS','PHONE_NO','CHECK-IN','ROOM TYPE'],tablefmt='psql'))
        elif(y==4):
            c1.execute("select * from booked")
            g=c1.fetchall()
            print(tabulate(g,headers=['REG.NO','NAME','ADDRESS','PHONE NO.','CHECK-IN','CHECK-OUT','NO.OF PEOPLE',
                                      'ROOM TYPE','STATUS'],tablefmt='psql'))
            
def employ():
    w='select * from employee' 
    c1.execute(w)
    s=c1.fetchall()
    print(tabulate(s,headers=["Employ No.","Name" ,"Gender" ,"Designation" ,"Contact"],tablefmt='psql'))
    for c in c1:
        print(c)
def delt():
    print("I hope your stay at our hotel was nice! ")
    v=int(input("Enter your registration number "))
    x='delete from booked where REG_NO="%s"'
    c1.execute(x,(v,))
    d1.commit()
    print("Your booking has been cancelled")
def hotel():
    print('''Star Hotel Group is a league of five star hotels spread accross India.We offer online booking of seats.,cancellation
and everything is just a click away.There are a variety of rooms available:
1-STANDARD:
1 Double Bed, Television, Telephone, Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and 
an attached washroom with hot/cold water
2-DOUBLE:
Room amenities include: 1 Double Bed, Television, Telephone Double-Door Cupboard, 1 Coffee table with 2 sofa, Balcony and 
an attached washroom with hot/cold water
3-DELUXE:
Room amenities include: 1 Double Bed + 1 Single Bed, Television,
Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofa,table, Balcony with an Accent table with 2 Chair ''')
    
while 1:
    import os
    from tabulate import tabulate
    l=[]
    J=[1046,1054,1056,1100,1102,1117,1158,1212,1220,1222,1232,1245,1313,1332,1562]
    R=[71,28,23,42,54,43,45,26,29,33,34,29,47,31,61,58]
    import mysql.connector
    d1=mysql.connector.connect(host="localhost",user="root",passwd="sonamgiri19")
    c1=d1.cursor()
    c1.execute('use hotel1')
    print()
    print('''                               WELCOME to the STAR HOTEL GROUP
Please choose the service ''')
    print('''    1.ABOUT STAR HOTEL GROUP
    2.BOOK A ROOM
    3.CHECK IN
    4.CHECK OUT
    5.MODIFY DETAILS                    
    6.CANCEL BOOKING                                       
    7.EMPLOYEES
    8.*ADMIN*(FOR HOTEL STAFF ONLY)
    9.EXIT''')
    print()

    a=int(input("Enter your choice "))
    print()
    if(a==1):
        hotel()
    elif(a==2):
        inpt()
    elif(a==3):
        ckin()
    elif(a==4):
        ckout()
    elif(a==5):
        modf()
    elif(a==6):
        delt()
    elif(a==7):
        employ()
    elif(a==8):
        adm()
    elif(a==9):
        exit()
    print()
    Y=input("WOULD YOU LIKE TO CONTINUE? ")
    if(Y=='Y'):
        os.system("cls");
        continue
    elif(Y!='Y'):
        print("Thanks for using!!!!!")
        break
    
