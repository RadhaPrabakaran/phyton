# # for a in range(3,20):
# #     print(a,end=" ")


# # # Exercise 1: Print first 10 natural numbers using for loop
# # for x in range(1,11):
# #     print(x, end=" ")
# # print("")

# # # Exercise 2: Calculate sum of all numbers from 1 to a given number
# # sum=0
# # b = int(input("Enter the number"))
# # for a in range(b+1):
# #     sum+= a
# # print( "sum of numbers", sum)

# # # Exercise 3: Print multiplication table of a given number
# c = int(input("Enter the number"))
# for a in range(1,11):
#    print(c*a)
# print ("Done")
# # # Exercise 4: Display a message “Done” after the successful execution of the for loop

# # # Exercise 5: Display numbers from -10 to -1 using for loop
# for i in range(-10,0):
#    print(i)

# While loop
# i=4
# while i<10:
#     print(i, end=" ")
#     i+=1

# Exercise 1: Print first 10 natural numbers using while loop
i=1
while i<=10:
    print(i, end=" ")
    i+=1
# Exercise 2: Calculate sum of all numbers from 1 to a given number
sum=0
b = 1
while b<=10:
  sum+= b
  b+=1
  print( "sum of numbers", sum)


# Exercise 3: Print multiplication table of a given number
c = 1
mul = 7
while c<=10:
   print(c*mul)
   c+=1


# Exercise 4: Count the total number of digits in a number
x = int(input("Enter a number"))
total = 0
while x != 0:
    x = x // 10
    total += 1
print(total)
