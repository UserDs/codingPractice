def reverse_list_2(list):
	n = len(list)
	for i in range(0,n/2):
		list[i],list[n-i-1]=list[n-i-1],list[i]
	return list

print (reverse_list_2([1,2,3,4]))
print (reverse_list_2([4,6,4,7,9,0]))
