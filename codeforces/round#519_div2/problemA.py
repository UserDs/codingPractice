n = int(input())
ai = list(map(int, input().split()))
opposite_votes = sum(ai)
k = max(ai)
my_votes = k * n - opposite_votes
while(my_votes <= opposite_votes):
	k = k + 1	
	my_votes = k * n - opposite_votes
print(k)
	