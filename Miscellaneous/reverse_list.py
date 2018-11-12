def reverse_list(list):
	a = []
	for i in range(len(list)-1,-1,-1):
		a.append(list[i])
	return a

print (reverse_list([1,2,3,4]))
print (reverse_list([4,6,4,7,9,0]))
