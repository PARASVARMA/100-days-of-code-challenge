#Encapsulation or Data hiding concept:-
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)



#In Encapsulation attributes with double underscore:

class Spam:
  __egg = 7
  def print_egg(self):
    print(self.__egg)
s = Spam()
s.print_egg()
print(s._Spam__egg)
print(s.__egg)
