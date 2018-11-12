def maximum(str):
	count = str.count(str[0])
	index = 0
	for i in range (1,len(str)):
		count1 = str.count(str[i])
		if count1>count:
			index = i
			count = count1
		if count1==count:
			if ord(str[i])<ord(str[index]):
				index = i
	return str[index]
input_string = 'cbbbbccc'
print(maximum(input_string))