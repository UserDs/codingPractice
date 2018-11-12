input_numbers = list(map(int, input().split()))
# number oftest cases t
t = input_numbers[0]

# maximum given value of n 
max_n = max(input_numbers[1:])

answer_list = [1, 2]

for i in range(1, max_n):
	current_length = len(answer_list)
	# as_integer_ratio() function convert a fraction to integer ratio
	fraction_as_tuple = ((answer_list[current_length-2] / answer_list[current_length-1]) + (-1)**(i) * (( 1 / answer_list[current_length-1]) / 2)).as_integer_ratio()
	answer_list.append(fraction_as_tuple[0])
	answer_list.append(fraction_as_tuple[1])

for i in range(1, t+1):
	index = 2 * input_numbers[i] - 2
	print(answer_list[index])
	print(answer_list[index + 1])

