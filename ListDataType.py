# List Data Types in Python
'''
- List items are ordered, changeable, and allow duplicate values.
- List items are indexed, the first item has index [0], the second item has index [1] etc.
- The lists are ordered, it means that the items have a defined order, and that order will not change.
- If you add new items to a list, the new items will be placed at the end of the list.
- A list can contain different data types exmaple :- myList = list1 = ["abc", 34, True, 40, "male"]
'''

myList = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(myList))  # print the numbers of element of the list
print(type(myList))  # print the typ of object in this case list.
print(myList)

# Creating List Using List Constructor
myList1 = list(("apple", "banana", "cherry"))
print(myList1)

# Accessing the List Items
print(myList1[0])  # accessing the list element using index
print(myList1[-1])  # accessing the list element using negative indexing
'''Negative Indexing : starting from end. like index[-1] =cherry index[-2] = banana like that '''

# Ranging of Indexes
'''we can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.'''
myList2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(myList2[2:5])  # The search will start at index 2 (included) and end at index 5 (not included).
print(myList2[:4])  # This list start print from begining upto 3 index exclude 4th index.
print(myList2[2:])  # this start printing the elements from 2 index and printing upto last index.
print(myList2[-4:-1])  # negative indexing used

if "apple" in myList2:
    print("Yes")  # print Yes if present in list.

# Change Item Values
myList3 = ["apple", "banana", "cherry"]
myList3[1] = "kiwi"
print(myList3)  # its will replace the values ate intex 1 with kiwi

myList4 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
myList4[1:3] = ["blackcurrant", "watermelon"]
print(myList4)  # change the value of items within a specific range.

myLis5 = ["apple", "banana", "cherry"]
myLis5[1:2] = ["blackcurrant", "watermelon"]
print(myLis5)  # Change the second value by replacing it with two new values

myList6 = ["apple", "banana", "cherry"]
myList6[1:3] = ["watermelon"]
print(myList6)  # Change the second and third value by replacing it with one value .O/p  ['apple', 'watermelon']

myList7 = ["apple", "banana", "cherry"]
myList7.insert(2, "watermelon")
print(myList7)  # The insert() method inserts an item at the specified index.

#Add Elemnets to List
myList8 = ["apple", "banana", "cherry"]
myList8.append("orange")
print(myList8) # add an item to the end of the list

myList_A = ["apple", "banana", "cherry"]
myList_B = ["mango", "pineapple", "papaya"]
myList_A.extend(myList_B) #append elements from another list to the current list. We can add any iterable object (tuples, sets, dictionaries etc.)
print(myList_A)

#Remove Elements from List
myList9 = ["apple", "banana", "cherry"]
myList9.remove("banana") #remove the 'banana' from the list
print(myList9)
'''Note:- If there are more than one item with the specified value, the remove() method removes the first occurance'''

myList10 = ["apple", "banana", "cherry"]
myList10.pop(1) #removes the specified index
print(myList10)
'''Note:- If you do not specify the index, the pop() method removes the last item.'''

myList11 = ["apple", "banana", "cherry"]
del myList11[0] #removes the specified index. The del keyword can also delete the list completely.
print(myList11)

myList12 = ["apple", "banana", "cherry"]
myList12.clear() #empties the list. The list still remains, but it has no content.
print(myList12)

#Loop  Lists
myList13 = ["apple", "banana", "cherry"]
for x in myList13: #Print all items in the list, one by one
  print(x)

myList14 = ["apple", "banana", "cherry"]
for i in range(len(myList14)):
  print(myList14[i])