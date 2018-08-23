#Itertools:-
from itertools import count

for i in count(3):
  print(i)
  if i >=11:
    break


#Prediction function of itertools:
from itertools import accumulate, takewhile

nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x<= 6, nums)))


#Product and permutation function:
from itertools import product, permutations

letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
