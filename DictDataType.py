'''Dictionary Data Type In Python'''
'''-Dictionaries are used to store data values in key:value pairs.
- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
- dictionaries are ordered, it means that the items have a defined order.
- Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
- Dictionaries are written with curly brackets, and have keys and values.
- The values in dictionary items can be of any data type.
'''

myDict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#Create Dict using constructor
myDict1 = dict(name = "John", age = 36, country = "Norway")
print(myDict1)


check={
    "name":"Amardeep",
    "number":"9112499967",
    "address":"Pune",
}

print(check)
print(type(check)) # print the type of object we are using in this case dict.
print(len(check)) # if it have same key(like name)it will count it as one so it will print 3.
#Accessing Items in Dictionary
print(check["number"]) #we can access the items of a dictionary by referring to its key name, inside square brackets
print(check.get("name")) #presented in key:value pairs, and can be referred to by using the key name.

print(check.keys()) # will return a list of all the keys in the dictionary
check['colour'] = 'white' # we can add new key:value paire to dict

#Can Update The dict in these ways
check.update(brother="Pankaj") # this aldo update the Dict
check.update({"address":"Pune-17"})
check["sport"] = 'cricket' # can add the key:values in the like this.



print(check.values()) # will return a list of all the values in the dictionary
print(check.items()) #will return each item in a dictionary, as tuples in a list. i.e
#([('name', 'Amardeep'), ('number', '9112499967'), ('address', 'Pune'), ('colour', 'white')])

if "brother" in check: #check if this brother is prensent in the dict; Note we can not check with values if its is prensent in dict or not
    print("Yes")

print(check.pop("address")) #removes the item with the specified key name

print(check.popitem()) #emoves the last inserted item in this case "sport":"cricket" will get removed

del check["brother"] #removes the item with the specified key name
'''del check #delete the dictionary completely'''

'''check.clear() # empties the dict'''

for x in check: #Print all key names in the dictionary, one by one
    print(x)

for x in check.keys(): #Print all key names in the dictionary, one by one
    print(x)

for x in check: #Print all values in the dictionary, one by one
    print(check[x])

for x in check.values(): #Print all values in the dictionary, one by one
    print(x)

for x, y in check.items():
    print(x,y)
'''print like this
name Amardeep
number 9112499967
colour white'''
print(check)

myDict2 = check.copy() #copy of a dictionary with the copy() method
print(myDict2)

myDict3 = dict(check) #make a copy is to use the built-in function dict()
print(myDict3)

#Nested Dict Concept
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(print(myfamily["child2"]["name"])) # access items from a nested dictionary