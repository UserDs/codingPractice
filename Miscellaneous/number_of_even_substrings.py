def even_substrings(string):
	n = len(string)
	count = 0
	for i in range (0,n):
		if int(string[i])%2 == 0:
			count = count + (i+1)
	return count

print(even_substrings('1234'))
print(even_substrings('154'))
print(even_substrings('15'))