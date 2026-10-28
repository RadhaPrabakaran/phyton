# Exercise 1: Basic Dictionary Operations
a={"Name":"Rad","Age":33}
a["Location"]="Chennai"
print(a)
a["Name"] ="Radha"
print(a)
del a["Age"]
print(a)
print(a["Location"])
# Exercise 2: Dictionary Operations
xa={"Name":"Rad","Age":33}
del xa["Age"]
print("Delete a List of Keys",xa)
# Exercise 3: Dictionary from Two Lists
names =["Alice","Bob","Charlie"]
location=["Chennai","Mumbai","Kolkata"]
Dic = {names:location for names,location in zip(names,location)}
print("Dictionary from Two Lists ", Dic)
# Exercise 4: Clear Dictionary
print("Clear Dictionary", location.clear())
# Exercise 5: Merge Dictionaries
Dic1 ={'a':1,'b':2}
Dic2 ={'c':3,'d':4}
print("Merge Dictionaries", Dic1|Dic2)
# Exercise 6: Access Nested Dictionary
print("Access Nested Dictionary",names[1][2])
# Exercise 7: Access ‘history’ Key From a Nested Dictionary
Emp_rec={"Name":"Rad","Age":33,"Location":"Chennai"}
print("Access Location From a Nested Dictionary",Emp_rec.get("Location"))
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print("Access history Key From a Nested Dictionary",student["grades"]["history"])
# Exercise 8: Initialize Dictionary with Default Values
z={"Bob","Rad","Ali"}
Defaultval=0
print("Initialize Dictionary with Default Values",dict.fromkeys(z,Defaultval))
# Exercise 9: Rename a Key of Dictionary
a={"Name":"Rad","Age":33}
a["Empname"]=a.pop("Name")
print("Rename a Key of Dictionary",a)
# Exercise 10: Delete a List of Keys
x={"Name":"Rad","Age":33,"Location":"Chennai","State":"TN"}
z=["Age","Location"]
for key in z:
    x.pop(key,None)
print("Delete a Key of Dictionary",x)


