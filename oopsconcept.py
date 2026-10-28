# class A:
#     a=11
#     def m(self):
#         print("uncode")
# # print(A.a)
# # A.m() 
# obj=A()
# print(obj.a)
# obj.m()      

# Exercise on Car

# class Car:
#     # Class atribute
#     wheels=4

#     # Constructor
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model
#     # Method
#     def display_info(self):
#         print(f"{self.brand} {self.model} has {self.wheels}")    
# my_car= Car("Toyata","Corolla")
# my_car.display_info()

# class X:
#     def __init__(self,a,b):
#         print("Uncode")
#         print(a+b)
# obj=X(12,34)        

#Inheritance

# class Animal:
#     def speak(self):
#         print("Animal speaks")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")
# dog=Dog()
# dog.speak() 

# class A:
#    a=22 
# class B(A):
#    b=33
# class C(B):
#    c=77
# obj=C()
# print(obj.a)
# print(obj.b)
# print(obj.c)

#Encapsulation
# class Car:
#     def __init__(self,brand,speed):
#         self.__brand =brand
#         self.__speed =speed


# #polymorphism - method overloading

# class Cat:
#     def speak(self):
#         print("Meow")

# class Dog:
#     def speak(self):
#         print("woof")

# animals=[Cat(),Dog()]   

# for animal in animals:
#  animal.speak()            



#polymorphism - method overwritting
class A:
     def m(self):
         print("Black Car")

class b(A):
        def m(self):
            print("Red Car") 
obj=b()
obj.m()
              

