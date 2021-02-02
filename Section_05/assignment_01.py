# Assignment 1:

"""
Define a class hierarchy representing animals with a parent class Animal
and child classes such as dog, fish and bird. Each subclass animal should have
a name and an age and should have 2 methods defined in it: move(), eat().
The move method needs to be specific for a given animal where as the
eat() method should be generic for all animals. The methods don't need to
do anything except print information about who is doing what.

After creating the class hierarchy, create instances of each of the 3 animals
dog, fish and bird and make them eat and move.

"""

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def move(self):
        print("This needs to be overwritten.")

    def eat(self):
        print(self.name + " is eating!")

class Dog(Animal):

    def move(self):
        print("Dog is moving")

class Fish(Animal):

    def move(self):
        print("Fish is moving")

class Bird(Animal):

    def move(self):
        print("Bird is moving")

dog1 = Dog("Rex", 5)
fish1 = Fish("Gold fish", 2)
bird1 = Bird("Parrot", 3)

for ob in [dog1, fish1, bird1]:
    ob.move()
    ob.eat()