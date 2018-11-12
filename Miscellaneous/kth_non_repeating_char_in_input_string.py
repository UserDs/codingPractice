import string 
def kth_nonrepeating(string,k):
	n = len(string)
	count = 0
	for i in range (0,n):
		if string[i] in string[:i]+string[i+1:] == False:
			count = count +1
			if count == k:
				return string[i]
	return "Less than k non-repeating characters"

print(kth_nonrepeating('geeksforgeeks',1))
print(kth_nonrepeating('geeksforgeeks',2))
print(kth_nonrepeating('geeksforgeeks',3))
print(kth_nonrepeating('geeksforgeeks',4))
print(kth_nonrepeating('geeksforgeeks',5))
