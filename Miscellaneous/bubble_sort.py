def bubble_sort(myList):
	for i in range (len(myList)-1,0,-1):
		for j in range (1,i+1):
			if myList[j-1]>myList[j]:
				myList[j-1],myList[j] = myList[j],myList[j-1]
numbers = [1,4,3,6,86,2354,245,53,43]
bubble_sort(numbers)
print(numbers)


