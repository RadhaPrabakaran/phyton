# Exercise 1: Basic Set Operations
a={12,12,12,3.5,3.5,1,0,True,False,"uncode"}
print("set",a)
a.add(44)
print("Add element in set",a)
a.discard(12)
print("Discard an element in set",a)
a.remove(3.5)
print("Remove an element in a set",a)
# Exercise 2: Clear All Elements
a.clear()
print("Clear all element in a set",a)
# Exercise 3: Find the Length of a Set
z={10,20,30,40,50,60,70,80,90}
print(" Find the Length of a Set",len(z))
# Exercise 4: Check if a Set is Empty
b={1,2,3,4,5,6,70,80}
if len(a)==0:
 print("The List is empty")
else:
 print("The List is not empty")
# Exercise 5: Union of Sets
union1=b|z
print("Union of Sets", union1)
# Exercise 6: Intersection of Sets
inter=b&z
print("intersection of Sets", inter)
# Exercise 7: Difference of Sets
print(" Difference of Sets", b-z)
# Exercise 8: Symmetric Difference
print(" Symmetric Difference of Sets", b^z)
# Exercise 9: Find Max and Min
print(" max of Sets", max(z))
print(" min of Sets", min(z))
# Exercise 10: Sum of Set Elements
print(" Sum of Sets", sum(b))