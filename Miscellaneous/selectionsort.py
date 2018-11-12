def selection_sort(numbers):
	for i in range (0,len(numbers)-1):
		for j in range (i+1,len(numbers)):
			if numbers[i]>numbers[j]:
				temp = numbers[i]
				numbers[i] = numbers[j]
				numbers[j] = temp
		
numbers1 = raw_input("Enter the numbers to be sorted: ")
numbers = numbers1.split(',')
print(numbers)
#numbers = [2,5,4,3,5667,25,314]
selection_sort(numbers)
print(numbers)

