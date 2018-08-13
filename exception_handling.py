try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occured")
    print("due to zero division")

    #example of exception handling:=
    try:
        variable = 10
        print(10 / 2)
    except ZeroDivisionError:
        print("Error")
        print("Finished")#this will give the output 5.0

#Exception handling other program:-
try:
    variable = 10
    print(variable + "hello")
    prinr(variable / 2)
except ZeroDivisionError:
    print("Division by zero")
except (ValueError, TypeError):
    print("Error occurred")
