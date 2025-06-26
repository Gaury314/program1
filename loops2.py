# #while true condition
# while True:
#     print("1.ADDITION")
#     print("2.SUBTRACTION")
#     print("3.MULTIPLICATION")
#     print("4.DIVISION")
#     print("5.exit")
#     choice=int(input("enter your choice:"))
#     num=0
#     if choice==1:
#         a=int (input("enter the number="))
#         b=int(input("enter the second number="))

#         print("sum=",a+b) 
#     elif choice==2:
#         a=int(input("enter the number="))
#         b=int(input("enter the number="))
#         print("sum=",a-b)   
#     elif choice==3:
#         a=int(input("enter the number="))
#         b=int(input("enter the number="))
#         print("sum=",a*b) 
#     elif choice==4:
#         a=int(input("enter the number="))
#         b=int(input("enter the number="))
#         if b!=0:
#             print("div=",a/b)
#         else:
#             print("not divisible!")
#     elif choice==5:
#         break
 #registration
 # while True:
 #     print("1:Registration")
 #     print("2:Login")
 #     print("3:Exit")
#     choice=str(input("enter your choice"))
#     if choice=="1":
#         name=(input("Enter your name:"))
#         Age=(input("Enter your age:"))
#         Address=(input("Enter your address:"))
#         Username=(input("Enter your username:"))
#         Password=(input("Enter your password:"))
#         print



    
choice=0
name=0
age=0
address=0
username=0
password=0
usrname=0
password2=0
while True:
    print("1.REGISTRATION")
    print("2.LOGIN")
    print("3.Exit")
    choice=int(input("enter your choice: "))
    if choice==1:
        name=(input("Enter your name:"))
        age=int(input("Enter your age:"))
        address=(input("Enter your address:"))
        username=(input("Enter your username:"))
        password=(input("Enter your password:"))
        phno=str(input("Enter your phone number:"))
    elif choice==2:
        usrname=(input("Enter the user name:"))
        password2=(input("Enter the password:"))
        b=18
        if usrname==username and password2==password and age>=18 and len(phno)==10:
            print("Name: ",name)
            print("Address:",address)
            print("Age:",age)
            print("Number:",phno)
        else:
            print("Invalid")   
    elif choice==3:
        break
    else:
        print("Invalid choice")

