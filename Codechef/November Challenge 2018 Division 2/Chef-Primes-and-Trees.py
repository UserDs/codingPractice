
def is_prime(num):
	if num > 1:
		for i in range(2, num):
			if num % i == 0:
				return "No"
		
		# this else will execute only if the index i in loop fail to be in the range (2, num)
		else:
			return "Yes"

	else:
		return "No"


n = int(input())

node_values = list(map(int, input().split()))

for i in range(0, n):
	if is_prime(node_values[i]) == "No":
		for j in range(1, n + 1):
			if j != i + 1:
				print(i + 1, j) 
		break
