#basic function example:-
def my_func():
    print("spam")
    print("spam")
    print("spam")
    my_func()

#function arguments:-
def print_with_exclamation(word):
    print(word + "!")
    print_with_exclamation("spam")
    print_with_exclamation("eggs")
    print_with_exclamation("python")

#function arguments with parameter:-
def print_sum_twice(x, y):
    print(x + y)
    print(x + y)
    print_sum_twice(5, 8)

#function arguments definition:-
def function(variable):
    variable += 1
    print(variable)
    function(7)
    print(variable)
