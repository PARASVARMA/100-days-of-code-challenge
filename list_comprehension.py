# a list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)

#other one examples:-
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

#Memory Error:-
even = [2*i for i in range(10**100)]