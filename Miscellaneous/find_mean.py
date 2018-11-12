def mean_of(myList):
	sum = 0
	for i in range (0,len(myList)):
		sum = sum + myList[i]
	return sum/len(myList)

numbers = [1,2,3,4,5]
print(mean_of(numbers))

