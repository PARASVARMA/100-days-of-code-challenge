#Lambdas:-
def my_func(f, arg):
  return f(arg)

my_func(lambda x: 2*x*x, 5)

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))


#Lambda funtion can be assigned to assigned to a variable:
double = lambda x: x * 2
print(double(7))
