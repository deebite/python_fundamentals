# Tuple in Python
"""
- Tuples are used to store multiple items in a single variable.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.
- Tuple items are ordered, unchangeable, and allow duplicate values.
- Tuple can store duplicate values.
"""

thistuple = ("apple", "banana", "cherry", "apple", "cherry",11,16)


print(thistuple) # print the tuple
print(type(thistuple)) # print type of object, in this t is tuple
print(len(thistuple)) # prints the numbers of element in the tuple.
print(thistuple[2:]) # print on based of the indexing value from index 2 to last element as we have not specidiy the any index for end
print(thistuple.count("apple")) # count how may 'apple' element present in tuple.
print(thistuple.index("banana")) # prints the nindex value of 'banana'.
y = ("chikoo",)
print(thistuple + y) # add chikoo to the tuple
checkList = list(thistuple) # make a list using list constructor.
checkList.remove("apple") # remove 'apple' from the tuple.
print(tuple(checkList)) # make the list into tuple using tuple constructor. tuple(("apple", "banana", "cherry"))
del thistuple # delete the tuple