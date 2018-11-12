def first_and_last(list,x):
	list1 = []
	for i in range(0,len(list)):
		if list[i] == x:
			list1.append(i)
			break
	for j in range(len(list)-1,-1,-1):
		if list[j] == x:
			list1.append(j)
			break
	return list1
print(first_and_last([1, 3, 5, 5, 5, 5 ,7, 123 ,125],7))
