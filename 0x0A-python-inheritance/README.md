# 0x0A. Python - Inheritance

Inheritance is a fundamental concept in object-oriented programming, including Python. It allows a new class to be created based on an existing class. The new class, known as the child class or subclass, inherits the attributes and methods of the parent class, also known as the superclass. This promotes code reusability and a logical structure for your code.
Here's a simple example in Python:

    class Parent:
        def method(self):
            print("This is from the parent class")

    class Child(Parent):
        pass

    c = Child()
    c.method()  # This will print: "This is from the parent class"

In this example, the Child class inherits from the Parent class, and thus it has access to the method defined in the Parent class. This is a basic example, but inheritance can be much more complex with multiple levels of inheritance and the ability to override methods in child classes.


## Files/Tasks

### 0. Lookup
0-lookup.py

### 1. My list
1-my_list.py, tests/1-my_list.txt

### 2. Exact same object
2-is_same_class.py

### 3. Same class or inherit from
3-is_kind_of_class.py

### 4. Only sub class of
4-inherits_from.py

### 5. Geometry module
5-base_geometry.py

### 6. Improve Geometry
6-base_geometry.py

### 7. Integer validator
7-base_geometry.py, tests/7-base_geometry.txt

### 8. Rectangle
8-rectangle.py

### 9. Full rectangle
9-rectangle.py

### 10. Square #1
10-square.py

### 11. Square #2
11-square.py
