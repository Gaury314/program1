# #Example using if statement
# age=101
# if age>=18:
#     print("you are an adult")
    
#     #Example using if-else statement
#     number=7
#     if number %2 ==0:
#         print("The number is even.")
#     else:
#         print("The number is odd.")

#         #Example using if-elif-else statement
#         score=-1
#         if score>=90:
#             print("grade:A")
#         elif score>=80:
#             print("grade:B")
#         elif score>=70:
#             print("grade:C")
#         else:
#             print("grade:below C")
  
i=20
if(i<15):
    print("i is smaller than 15")
    print("am in if block")
else:
    print("i is greater than 15")
    print("am in else block")
print("am not in if and not in else")
#example for nested if statement
i=14
if(i<20):
    if(i<12):
        print("i is smaller than 15")
    if(i<15):
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
ample for if elif else statement
i=20
if(i==10):
    print("i is 10")
elif(i==15):
    print("i is 15")
elif(i==20):
    print("i is 20")
else:
    print("i is not present")

score=100
if score<=100 and score>=0: 
    if score>=90:
        print("grade:A")
    elif score>=80:
        print("grade:B")  
    elif score>=70:
        print("grade:C")
    else:
        print("grade: below C")                 
else:
    print("invalid number")
