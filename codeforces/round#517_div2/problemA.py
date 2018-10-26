n, m, k, l = map(int, input().split())
# round = 1
# while( m*round <= n):
#     if (m*round - k) >= l:
#         return round
#     round = round + 1
# return -1
required = k  + l

per_friend = (required + m - 1) // m

if per_friend * m > n:
		print(-1)
else:
	print(per_friend)

