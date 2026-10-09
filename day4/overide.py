"""Method overriding in Python

Method overriding means a child class provides its own version of a method
that is already defined in its parent class.

This lets subclasses customize behavior while reusing the parent class.
"""


class Animal:
    def speak(self):
        print("Animal makes Sound")


class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak() # invoke parent class - To avoid methodoverriding


# Creating objects

#obj = Animal()
#obj.speak()

obj1 = Dog()
obj1.speak()

obj2 = Animal()
obj2.speak()