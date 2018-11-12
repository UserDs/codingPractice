n, k = map(int, input().split())
given_tree = [[0] * n for _ in range(n)]
for i in range(0, n - 1):
	row, column = map(int, input().split())
	given_tree[row - 1][column - 1] = 1
	given_tree[column - 1][row - 1] = 1

