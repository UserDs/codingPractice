def binary_search(sorted_list,x):

	n =len(sorted_list)
	if n==0:
		return 'Not found'
	if x == sorted_list[n/2]:
		return 'found'
	if x < sorted_list[n/2]:
		return binary_search(sorted_list[:n/2],x)
	if x > sorted_list[n/2]:
		return binary_search(sorted_list[n/2+1:],x)

print(binary_search([1,2,4,6,8,9],1))

print(binary_search([1,2,4,6,8,9],4))

print(binary_search([1,2,4,6,8,9],7))

print(binary_search([1,2,4,6,8,9],10))

print(binary_search([1,2,4,6,8,9,11],3))

print(binary_search([1,2,4,6,8,9,11],4))

print(binary_search([1,2,4,6,8,9,11],9))

print(binary_search([1,2,4,6,8,9,11],10))