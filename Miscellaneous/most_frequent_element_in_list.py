def maximum_element(list):
	current_max = list[0]
	for i in range(1,len(list)):
		if list[i] > current_max:
			current_max = list[i]
	return current_max
def most_frequent_in(list):
	element_list = []
	count_list = []
	for i in range(0,len(list)):
		
		if (list[i] in element_list) == False:
			element_list.append(list[i])
			count = 1
			for j in range(i+1,len(list)):
				if list[j] == list[i]:
					count = count+1
			count_list.append(count)
	
	#return element_list[0]
	c = []
	for k in range(0,len(element_list)):
		if count_list[k] == maximum_element(count_list):
			c.append(element_list[k])
	return c
print(most_frequent_in([1,5,4,3,2,5,7,3,5,6,5,3,5,3,3]))


