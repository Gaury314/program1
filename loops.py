# #while loop
# count=1
# while count<=5:
#     print(count)
#     count+=1


# count=1
# while count<=10:
#     if count%2==0:
#      print(count,"even")    
#     count+=1

# count=10
# while count>=1:
#     print(count)
#     count-=1
#     #calculator
# a=0
# i=int(input("enter  the number: "))
# while(i!=-1):
#     a=a+i
#     i=int(input("enter  the number: "))
# print(a)

#Sum of digits
# sum=0
# n=0
# i=int(input("enter a number:"))
# while i>0:
#     n=i%10
#     sum+=n
#     i=i//10
# print(sum)

# #check if the number is palindrome
# temp=0
# rev=0
# i=int(input("enter a number:"))
# temp=i
# while temp>0:
#     n=temp%10
#     rev=rev*10+n
#     temp=temp//10
# if rev==i:
#     print("It is a palindrome number")
# else:
#     print("It is not a palindrome number")

# # count the number of digits
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num //= 10  # Remove the last digit
#     count += 1  # Increment the count
# print("Number of digits:",count)

# #check for Armstrong number
# n=0
# sum=0
# i=int(input("enter a number:"))
# temp=i
# while temp>0:
#     n=temp%10
#     sum+=n**3
#     temp=temp//10
# if sum==i:
#     print("it is an armstrong number!")
# else:
#         print("it is not an armstrog number!") 
# print(range(15))
# print(list(range(15)))
# print(list(range(4,9)))
# print(list(range(5,25,4)))
# tuple_=("Python","Loops","Sequence","Condition","Range")
# for iterator in range(len(tuple_)):
#      print(tuple_[iterator].upper(),end=",")
# numbers=[4,6,7,3,5,8,10,6,1,9,2]
# square=0
# squares=[]
# for value in numbers:
#   square= value**2
#   squares.append(square)
# print("The list of squares is",squares)
 
string="python loop"
for s in string:
  if s=="o":
    print("if block")
else:
    print(s)
