def fibonacci_dp_1(n):
	lookup = [0]*(n+1)
	lookup[0] = 1
	lookup[1] = 1
	for i in range(2,n+1):
		lookup[i] = lookup[i-1] + lookup[i-2]

	return lookup[n]

#print(fibonacci_dp_1(2))
#print(fibonacci_dp_1(3))
#print(fibonacci_dp_1(4))
#print(fibonacci_dp_1(10))
#print(fibonacci_dp_1(15))
#print(fibonacci_dp_1(20)) 
print(fibonacci_dp_1(50)) 
