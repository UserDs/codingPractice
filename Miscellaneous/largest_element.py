def largest_in(myList):
	largest_at = 0
	for i in range (1,len(myList)):
		if myList[i]>myList[largest_at]:
			largest_at = i
	return myList[largest_at]

numbers = [1,3,5,3,4,7,9,6,44,67,4,3,6,77,3,56,34,234,63,45,3,6]
print (largest_in(numbers))
			