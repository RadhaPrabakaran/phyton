#Function
# def a(x,y):
#     print("Uncode")
#     print(x+y)
# def a1(x,y):
#     print(x+y)    
# a(1,3)
# a1(7,9)    

# # 1. Write a Python function to find the maximum of three numbers.
# def maxof3(a,b,c):
#  if a>b and a>c:
#     print("A is greatest of 3 numbers")
#  elif a<b and a>c:
#      print("B is greatest of 3 numbers")
#  else:
#    print("C is greatest of 3 numbers") 
# maxof3(22,11,55)
# # 2. Write a Python function to sum all the numbers in a list.
# def sum1(number):
#   return sum(number)
# x=[1,2,30]
# print("sum all the numbers in a list",sum1(x))      
# # 3. Write a Python function to multiply all the numbers in a list.
# def mul_list(my_list):
#     result = 1
#     for num in my_list:
#         result *= num
#     return result

# my_list = [2, 3, 4, 5]
# print(mul_list(my_list))
# # 4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
# def factorial(n):
#      if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers.")
#      elif n == 0 or n == 1:
#         return 1
#      else:
#         result = 1
#         for i in range(2, n + 1):
#             result *= i
#         return result
# print(factorial(4))
# # 5. Write a Python program to print the even numbers from a given list.
# def eve(b):
#  for i in b:
#   if i%2==0:
#    print( i,end=" ")
# b=[1,2,3,4,5,6]
# eve(b)

#Lambda Function:

a=lambda x,y:print(x+y)
a(11,22)

# Write a Python program to sort tuples using Lambda.
a=(2,5,3,66,1)
b=list(a)
x=sorted(b,key=lambda y:y)
print(tuple(x))

# Write a Python program to square and cube every number in a given list of integers using Lambda
numbers=[1,2,3,4,5]
square = list(map(lambda x:x**2,numbers))
print(square)
cube = list(map(lambda x:x**3,numbers))
print(cube)
# Write a Python program to count the even and odd numbers in a given list of integers using Lambda.
numbers=[1,21,3,4,5]
eve_num = len(list(filter(lambda x:x%2==0,numbers)))
print(eve_num)
odd_num = len(list(filter(lambda x:x%2!=0,numbers)))
print(odd_num)
# Write a Python program to add two given lists using map and lambda.
a=[1,2,3,4,5]
b=[6,7,8,9]
sum1= list(map(lambda x,y:x+y,a,b))
print(sum1)