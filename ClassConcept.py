# Object-Oriented Programming in Python
"""Major principles of object-oriented programming
- Class :- The class can be defined as a collection of objects. It is a logical entity that has some specific attributes and methods.
- Object :- The object is an entity that has state and behavior.Everything in Python is an object, and almost everything has attributes and methods.
- Method :- The method is a function that is associated with an object. In Python, a method is not unique to class instances. Any object type can have methods.
- Inheritance :- It specifies that the child object acquires all the properties and behaviors of the parent object.By using inheritance, we can create a class which uses all the properties and behavior of another class.
- Polymorphism :- By polymorphism, we understand that one task can be performed in different ways.
- Encapsulation :- It is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
- Data Abstraction :- Abstraction is used to hide internal details and show only functionalities.Data abstraction is achieved through encapsulation.
"""


class MyClass():

    def myfunction(self, name):
        print(f"Hi all myFunc printed {name}")


c1 = MyClass()
c1.myfunction("Amardeep")


# self :- The self-parameter refers to the current instance of the class and accesses the class variables. Note:- We
# can use anything instead of self, but it must be the first parameter of any function which belongs to the class.


class MyClass1():
    def __init__(self, name, age):  #
        self.name = name
        self.age = age


'''__init__ :- In order to make an instance of a class in Python, a specific function called __init__ is called. Although it is used to set the object's attributes, it is often referred to as a constructor.'''
c2 = MyClass1("Amardeep", 23)
print(c2.name, c2.age)


class Person():
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1


p = Person("Amardeep", 23)
p1 = Person("Lokare", 22)
print(Person.count, p.count, p.name, p.age) # 2 2 Amardeep 23
# count will be two because as we created two instance of the class.
