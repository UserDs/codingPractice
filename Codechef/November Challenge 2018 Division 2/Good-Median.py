import math

def all_even(input_integers):
	# input_integers.sort()
	all_even = 0
	for index1 in range(0, n-1):
		for index2 in range(index1 + 1, n):
			if input_integers[index1] == input_integers[index2]:
				all_even = all_even + min(index2, n - index2)		
	return all_even

def all_odd(input_integers):
	# input_integers.sort()
	all_odd = 0
	for i in range(1, n + 1, 2):
		all_odd = all_odd + ( math.factorial(n) / (math.factorial(n - i) * math.factorial(i)) )
	return int(all_odd)


t = int(input())

while(t > 0):
	n = int(input())
	input_integers = list(map(int, input().split()))
	input_integers.sort()
	# print(all_even(input_integers) + all_odd(input_integers))
	# print(total % 1000000007) 
	print((all_even(input_integers) + all_odd(input_integers)) % 1000000007)
	t = t - 1
	
