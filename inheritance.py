#Inheritance:-
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()


#Inheritance other example about super class and sub class:
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()


#Inheritance between three classes in which one is super class and other sub class and it also the super class of another second other:
class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_method()
c.third_method()
