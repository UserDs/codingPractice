def one_right_shift(input_list):
	n = len(input_list)
	new_list = []
	new_list.append(input_list[n-1])
	for i in range(0, n-1):
		new_list.append(input_list[i])
	return new_list

def lcs(sequence):
	n = len(sequence)
	current_max1 = 0
	current_max2 = 0
	for i in range(0, n):
		if sequence[i] == 0:
			if current_max2 > current_max1:
				current_max1 = current_max2
			current_max2 = 0
			if i == n - 1:
				break

		if sequence[i] == 1:
			current_max2 = current_max2 + 1
			if i == n - 1:
				if current_max2 > current_max1:
					current_max1 = current_max2
					break
	return min(current_max1,k)


n, q, k = map(int, input().split())
input_sequence = list(map(int, input().split()))
query_string = input()

for i in range(0, q):
	if query_string[i] == "?":
		store = lcs(input_sequence)
		print(store)
	if query_string[i] == "!":
		input_sequence = one_right_shift(input_sequence)


