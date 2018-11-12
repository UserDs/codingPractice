def remove_duplicates(list):
	list1 = []
	for i in range(0,len(list)):
		if (list[i] in list1) == False:
			list1.append(list[i])
			
	return list1

print(remove_duplicates([1,3,2,4,3,4,5,4,6,7,8,7,3,5,4,6,7,8,0,9,8,7,5,1,2,1,4,6,8,7,2,4,5,7,5,3,2,2,5]))

