#list slice:-
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])

#if the first number in a slice is omitted, it is taken to be the start of the list.
#if the second number is omitted, it is taken to be the end.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])
print(squares[7:])

#List slices can also have a third number, representing the step, to include only alternate values in the slice.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])
print(squares[2:8:3])
