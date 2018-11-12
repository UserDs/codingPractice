

def fibonacci_dp_2(n,lookup):
	
	if n==0 or n==1:
		lookup[n] = 1
	else:
		lookup[n] = fibonacci_dp_2(n-1,lookup) + fibonacci_dp_2(n-2,lookup)

	return lookup[n]

#print(fibonacci_dp_2(5,[None]*(101)))

#print(fibonacci_dp_2(20,[None]*(101)))


print(fibonacci_dp_2(50,[None]*(101)))
