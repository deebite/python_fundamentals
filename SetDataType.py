'''SET DATA TYPE IN PYTHON'''
'''Sets are used to store multiple items in a single variable.
- Set is one of 4 built-in data types in Python
- A set is a collection which is unordered, unchangeable*, and unindexed.
- Note: Set items are unchangeable, but you can remove items and add new items.
- Sets are written with curly brackets.(example:-{"apple", "banana", "cherry"})
- Duplicate values are not allowed in Set!
- we can add any Iterable object in Set.
'''
'''Unordered
- the items in a set do not have a defined order.
- Set items can appear in a different order every time you use them, 
and cannot be referred to by index or key.'''

'''Unchangeable
- Set items are unchangeable, meaning that we cannot change the items after the set has been created.
- Once a set is created, you cannot change its items, but you can remove items and add new items.
'''
'''Note:
- The values True and 1 are considered the same value in sets.
- The vlaues False and 0 are considered the same value  in sets.
'''
mySet = {"apple", "banana", "cherry", "apple"}
print(mySet) # will notprint duplicate values
print(len(mySet)) # it will not consider the duplicate values so it will print 3
print(type(mySet)) # print type of datatype i.e Set.

mySet1= {"abc", 34, True, 40, "male"}
print(mySet1) # can use elemet of different datatype like int String and float.

#Using Set Constructor
#-Use round brackets
mySet2 = set(("Amardeep", "Lokare", 91125,))
print(mySet2) #print set in any order as its is unorder

#Accessing Elements of Set
'''You cannot access items in a set by referring to an index or a key. because of unorder behavioure'''
mySet3 = {"Amardeep", "Lokare", 91125,56.7}
for x in mySet3:
    print(x) #print all the elements int the set.

print("Amardeep" in mySet3) # print True if "Amardeep" is present else False.

#Adding elemets in Set
mySet4 = {"apple", "banana", "cherry"}
mySet4.add("orange")
print(mySet4) #add "orange" in the set.but not sure at which index it will add as its is unordered.

#Update elements in Set
mySet5 = {"pineapple", "mango", "papaya"}
mySet5.update(mySet4)#this will insert the mySet4 element into mySet5. It will exclude the duplicate element
print(mySet5)

mySet6=["kiwi", "orange"] #this list datatype
mySet5.update(mySet6)
print(mySet5) # we can add any Iterable object to Set like in this case List we have added.

#Remove Element from Set(using discard and pop)
mySet7 = {"apple", "banana", "cherry"}
mySet7.discard("apple")
print(mySet7) #we use discard method to remove elemts from the set.

mySet7.pop() #this pop will remove any elemets from the set.
print(mySet7)

mySet7.clear() #it will make the set Empty and return like "set()"
print(mySet7)

'''del mySet7 --> it will delete the mySet7 and when we try to print it again it will give error mySet7 is not define'''

'''JOINS IN SET'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3=set1.union(set2) #returns a new set containing all items from both sets. Update methode do the same see above.
print(set3)
'''Note:- Both union() and update() will exclude any duplicate items.'''

#Keep ONLY the Duplicates methods
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z= x.intersection_update(y) #method will keep only the items that are present in both sets.
print(x) #prints {'apple'}

z = x.intersection(y) #return a new set, that only contains the items that are present in both sets
print(z) #print {'apple'}

#Keep All, But NOT the Duplicates
a = {"apple", "banana", "cherry"}
b = {"google", "microsoft", "apple"}
a.symmetric_difference_update(b) #method will keep only the elements that are NOT present in both sets.
print(a) #prints {'microsoft', 'google','banana','cherry'}

z = a.symmetric_difference(b) #method will return a new set, that contains only the elements that are NOT present in both sets.
print(a) #prints {'cherry', 'banana', 'microsoft', 'google'}

'''
- difference() - 	Returns a set containing the difference between two or more sets
- difference_update() - Removes the items in this set that are also included in another, specified set
- isdisjoint() - 	Returns whether two sets have a intersection or not
- issubset() - Returns whether another set contains this set or not
- issuperset() - Returns whether this set contains another set or not
'''
