sequence = list(map(int, input().split()))
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
print(current_max1)
