def add(a,b):
	return a+b
def subtract(a,b):
	return a-b
def multiply(a,b):
	return a*b
def divide(a,b):
	return a/b
choice = input("Please enter the choice: ")
number1 = float(input("number1: "))
number2 = float(input("number2: "))

if choice == add:
	print add(number1, number2)
elif choice == subtract:
	print subtract(number1, number2)
elif choice == multiply:
	print multiply(number1, number2)
elif choice == divide:
	print divide(number1, number2)
else:
	print ("Your choice is invalid")

