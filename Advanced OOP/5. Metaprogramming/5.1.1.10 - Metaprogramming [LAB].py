'''
Objectives

    improving the student's skills in operating with metaclasses;
    improving the student's skills in operating with class variables and class methods.

Scenario

    Imagine you've been given a task to clean up the code of a system developed in Python - the code should be treated as legacy code;
    the system was created by a group of volunteers who worked with no clear “clean coding” rules;
    the system suffers from a problem: we don't know in which order the classes are created, so it causes multiple dependency problems;
    your task is to prepare a metaclass that is responsible for:
        equipping all newly instantiated classes with time stamps, persisted in a class attribute named instantiation_time;
        equipping all newly instantiated classes with the get_instantiation_time() method. The method should return the value of the class attribute instantiation_time.

* The metaclass should have its own class variable (a list) that contains a list of the names of the classes instantiated by the metaclass (tip: append the class name in the __new__ method).

    Your metaclass should be used to create a few distinct legacy classes;
    create objects based on the classes;
    list the class names that are instantiated by your metaclass.
'''

import datetime
import time

# Helper Function for InstantiationMeta meta class
def get_instantiation_time(self):
    return self.instantiation_time

# Helper Meta Class
class InstantiationMeta(type):
    # Create meta class attribute
    __classes_instantiated__ = list()
    
    def __new__(mcs, name, bases, dictionary):
        # Add class to list of classes instantiated
        mcs.__classes_instantiated__.append(name)
        
        # Add time instantiated
        if 'instantiation_time' not in dictionary:
            dictionary['instantiation_time'] = datetime.datetime.now()
        
        # Add link to get instantiated funtion
        if 'get_instantiation_time' not in dictionary:
            dictionary['get_instantiation_time'] = get_instantiation_time
        
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj

# === TESTING CLASSES ===
class Dog(metaclass=InstantiationMeta):
    def __init__(self, name) -> None:
        self.name = name
    
    def bark(self):
        print("Wooof!")
        

class Cat(metaclass=InstantiationMeta):
    def __init__(self, name) -> None:
        self.name = name
    
    def meow(self):
        print("Meow!")


# === FUNCTIONALITY TESTING ===
dog1 = Dog("Buddy")
print(dog1.get_instantiation_time())
time.sleep(3)
print(dog1.instantiation_time)
time.sleep(3)
print(f"Now: {datetime.datetime.now()}")

print(InstantiationMeta.__dict__['__classes_instantiated__'])