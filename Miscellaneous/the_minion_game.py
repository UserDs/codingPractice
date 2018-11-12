def minion_game(string):
	n = len(string)
	kevin_scores = 0
	for i in range(0,n):
		if string[i] in ['A','E','I','O','U']:
			kevin_scores = kevin_scores+(n-i)
	stuart_scores = (n*(n+1)/2)-kevin_scores
	if kevin_scores > stuart_scores:
		return 'Kevin '+ str(kevin_scores)
	if stuart_scores > kevin_scores:
		return 'Stuart '+str(stuart_scores)
	if stuart_scores == kevin_scores:
		return 'Draw'

print(minion_game('DEEPAK'))
print(minion_game('ARIJIT'))
print(minion_game('FRICTION'))
print(minion_game('KTGL'))
print(minion_game('AEIO'))
print(minion_game('BANAASA'))


