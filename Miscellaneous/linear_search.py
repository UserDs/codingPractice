def linear_search(myList,x):
	for i in range (0,len(myList)):
		if myList[i]==x:
			return "Yes"
	return "No"
#numbers1 = raw_input("Enter the numbers to be sorted: ")
#numbers = numbers1.split(',')
#print(numbers)  
numbers = [2,5,4,6,8,7,9]
print (linear_search(numbers,1))
print (linear_search(numbers,2))
print (linear_search(numbers,3))
print (linear_search(numbers,4))
print (linear_search(numbers,5))
print (linear_search(numbers,6))
