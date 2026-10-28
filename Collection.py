# # String
# # a="Radha"
# # b=33

# # print(a+str(b))
# # print(a,b)
# # for i in a:
# #     print(i,end=" ")
# #     print()
# # print(f"My name is{a} and my age is{b}") 
# # print(a.upper())   
# # print(a.replace("a"," "))

# # List
# # 

# # Exercise 1. Perform Basic List Operations
# a=[10,12,14.5,"Uncode",True]

# print(a)
# print(a[2])
# print(a[1:4])
# print(a[::-1])

# # Exercise 2. Perform List Manipulation

# # Exercise 3. Sum and Average of All Numbers in a List
# a=[1,2,3,4,5]
# sum = sum(a)
# length =len(a)
# Avg = sum/length
# print(f"Sum = {sum} and Average = {Avg}")
# # Exercise 4. Find Maximum and Minimum from List
# b =[22,32,44,10,5,]
# maximum = max(b)
# minimum = min(b)
# print(f"Max = {maximum} and Min = {minimum}")
# # Exercise 5. Calculate the Product of All Elements
# mul =1
# for i in b:
#  mul=mul*i
#  print(f"Calculate the Product of All Elements {mul}")
# # Exercise 6. Count Even and Odd Numbers
# for i in b:
#  if i%2==0:
#   print( i," number is even")
#  else:
#   print( i, "number is odd")
# # Exercise 7. Reverse a List
# b =[22,32,44,10,5,]
# print("Reverse a List", b[::-1])
# # Exercise 8. Sort a List of Numbers
# b.sort()
# print("Sort a List",b)
# # Exercise 9. Create a Copy of a List
# c=b.copy()
# print("Copy of a List",c)

# # Exercise 10. Combine Two Lists
# print("Combine Two Lists",a+b)

# # Access the third element of a list
# a=[1,2,3,4,5,6,7,8]
# print("Access the third element of a list",a[2])
# # List Length: Print the total number of items

# print(len(a))
# # Check if the list is empty

# a=[1,2,3,4,5,6,7,8]
# b=[]

# if len(b)==0:
#  print("The List is empty")
# else:
#  print("The List is not empty")

# # Change Element: Change the second element of a list to 200 and print the updated list.
# a=[1,2,3,4,5,6,7,8]
# a[1]=200
# print(a)
# # Append Element: Add 600 o the end of a list and print the new list.
# a.append(600)
# print(a)
# # Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
# a.insert(2,300)
# print(a)
# # Remove Element (by value): Remove 600 from the list and print the list.
# a.remove(600)
# print(a)
# # Remove Element (by index): Remove the element at index 0 from the list print the list.
# a.pop(0)
# print(a)

# Tuple:




# Exercise 1: Basic Tuple Operations
a=(1,5.5,"Uncode",True)
print(a[1])
print(a[2][3])
print(a[::-1])
# Exercise 2: The Trailing Comma
a=(22,)
print(type(a))
# Exercise 3: Tuple Repetition
b=(12,34,56)
print("Tuple Repetition", b*3)
# Exercise 4: Tuple Concatenation
x=("a","b","c")
y=(9,8,7)
print("Tuple Concatenation",x+y)
# Exercise 5: Tuple Slicing
z=(10,20,30,40,50,60,70,80,90)
print("Tuple Slicing 1", z[2:5])
print("Tuple Slicing 2", z[:7])
# Exercise 6: Tuple Reversal
print("Tuple Reversal ",z[::-1])
# Exercise 7: Counting
print("Counting", z.__len__())
# Exercise 8: Tuple Unpacking
y=(9,8,7)
a,b,c = y
print(a,b,c)
# Exercise 9: The Swap Trick
a=(1,2,3)
b=("a","b","c")
a,b=b,a
print(a,b)
# Exercise 10: Nested Tuple Access
a=(1,5.5,"Uncode",True)
print(" Nested Tuple Access ", a[2][3])