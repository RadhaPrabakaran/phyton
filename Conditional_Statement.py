# a=75
# if a>=100:
#     print("a is greater than equal to 25")

# else:
#     print("a is not greater than equal to 25")


# age = 5
# if age>=18 and age <22:
#     print("Eligible for Voting")
# elif age>=21:
#     print("Eligible for voting and participating")
# else:
#     print("Not eligible ")  

# type casting
# age = int(input("Enter the age"))

# if age >=21:
#     print("Eligible for Voting and  participating in election")
# elif age>= 18 and age <21:
#     print("Eligible for Voting and not eligible for participating in election")    
# else:
#     print("Not eligible ")    


# WAP to find greatest of 3 numbers a=10,b=27,c=6.

a=10
b=27
c=6

if a>b and a>c:
    print("A is greatest of 3 numbers")
elif a<b and a>c:
     print("B is greatest of 3 numbers")
else:
   print("C is greatest of 3 numbers")
# WAP to check whether 10 is divisible in both 2 and 4.
a=10
b=2
c=4

if a%b==0 and a%c==0: 
     print("10 is divisible in both 2 and 4")
else:
     print("10 is not divisible in both 2 and 4.")    
# WAP to check whether 8 is divisible in either 3 or 4.

a=8

if a%3 ==0: 
  if a%4==0:
    print(" 8 is divisible by 3 and 4")
  else:
    print(" 8 is divisible by 3")
elif a%4==0:
    if a%3==0:
        print(" 8 is divisible by 3 and 4")
    else:
        print(" 8 is divisible by 4")

#         WAP to print Grades:
# Grade A: if marks is beteween 76 and 100
# Grade B: if marks is beteween  51 and 75
# Grade C: if marks is beteween 26 and 50
# Grade D: if marks is beteween 0 and 25

a=35
if a>=76 and a<=100:
    print("Grade A")
if a>=51 and a<=75:
    print("Grade B")
if a>=26 and a<=50:
    print("Grade C") 
if a<0 and a<=25:
    print("Grade D")       
# Write a Python program to check if a number is positive, negative, or zero.
a = int(input("Enter the number"))
if a>0:
    print("positive number")
elif a<0:
    print("Negative number")
else:
     print("Zero")

# Write a Python code to check if a number is even or odd
a = int(input("Enter the number"))
if a%2==0:
    print("number is even")
else:
    print("number is Odd")
# Write a Python program to find the maximum of three numbers
a = int(input("Enter the number"))
b = int(input("Enter the number"))
c = int(input("Enter the number"))
if a>b and a>c:
    print("A is greatest of 3 numbers")
elif a<b and a>c:
     print("B is greatest of 3 numbers")
else:
   print("C is greatest of 3 numbers")