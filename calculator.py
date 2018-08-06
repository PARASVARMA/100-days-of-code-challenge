#This calculator is coded by python
print("select the operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")
choice = input("enter the choice(1/2/3/4):")
num1 = int(input("enter the first no."))
num2 = int(input("enter the second no."))

if choice == '1':
    print(num1 + num2)

elif choice == '2':
    print(num1 - num2)

elif choice == '3':
    print(num1 * num2)

elif choice == '4':
    print(num1 / num2)

elif choice == '5':
   print(num1 % num2)

else:
    print("this is not valid input")
