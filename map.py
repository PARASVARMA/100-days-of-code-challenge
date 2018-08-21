#Map:-
def add_five(x):
  return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#other example of map:
nums = [11, 22, 33]
a = list(map(lambda  x: x*2 , nums ))
