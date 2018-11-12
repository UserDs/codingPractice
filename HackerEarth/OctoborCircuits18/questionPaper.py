
t = int(input())
while(t > 0):
	possible_marks = set()
	n, a, b = map(int, input().split())
	for correct in range(0, n + 1):
		for incorrect in range(0 , n - correct + 1):
			next_possible = correct * a - incorrect * b
			possible_marks.add(next_possible)
	print(len(possible_marks))
	t = t - 1
