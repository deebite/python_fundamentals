thistuple = ("apple", "banana", "cherry", "apple", "cherry",11,16)

print(thistuple)
print(type(11))
print(len(thistuple))
print(thistuple[2:])
print(thistuple.count("apple"))
print(thistuple.index("banana"))
y = ("chikoo",)
print(thistuple + y)
checkList = list(thistuple)
checkList.remove("apple")
print(tuple(checkList))
del thistuple