#Dictionary:-
ages = {"Dave": 24, "mary": 43, "john": 56}
print(ages["Dave"])
print(ages["mary"])

#this example of dictionary returns a keyerror:
primary = {
    "red": [25, 0, 0],
    "green": [0, 25, 0],
    "blue": [0, 0, 25],
}
print(primary["red"])
print(primary["yellow"])

 #immutable objects:-
 bad_dict = {
     [1, 2, 3]: "one two three",
 }