num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

def find_gcd(a,b):
	if b==0:
		return a;
	if a>b:
		a=a-b
		return find_gcd(a,b)
	if a<= b:
		b=b-a;
		return find_gcd(a,b)

print "The gcd of", num1, "and", num2, "is", find_gcd(num1,num2)


