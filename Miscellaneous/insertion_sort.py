def insertion_sort(myList):
	for i in range (1,len(myList)):
		for j in range (i-1,-1,-1):
			if myList[j]>myList[j+1]:
				myList[j],myList[j+1] = myList[j+1],myList[j]
numbers = [1, 3, 4, 6, 43, 53, 86, 245, 2354]
insertion_sort(numbers)
print(numbers)
