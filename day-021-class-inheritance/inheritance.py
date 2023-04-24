# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

'''
Inheritance
'''

class Animal:
    def __init__(self):
        # all animals have two eyes
        self.num_eyes = 2

    def breathe(self):
        # all animals breath
        print("inhales, exhales.")

# 'Animal' in inheritance is class to inherit from
# fish is type of an animal that also swims
class Fish(Animal):
    # initializer
    def __init__(self):
        # refers to the superclass to inherit all attributes and methods
        # call to super() in the initializer is recommended, but not strictly required
        super().__init__()

    def breathe(self):
        super().breathe()
        print("fish breathes underwater.")

    def swim(self):
        print("fish is moving in water.")

nemo = Fish()
print("fish has", nemo.num_eyes, "eyes.")
nemo.breathe()
nemo.swim()
