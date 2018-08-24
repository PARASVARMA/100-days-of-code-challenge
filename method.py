#Method in Python:-
class Dog:
  def __init__(self, name, color):
    self.name = name
    self.color = color

  def bark(self):
    print("Woof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

#Other example:
class Student:
    def __init__(self, name):
     self.name = name
 def sayHi(self):
    print("Hi from " +self.name)
s1 = Student("Amy")
s1.sayHi()