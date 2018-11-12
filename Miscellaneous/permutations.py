def toString(list): # ['a', 'b', 'c'] => 'abc'
	return ''.join(list)

	
def permutations(a,l,r):
	if l == r:
		print toString(a)
	else:
 		for i in range(l,r+1):
 			a[i],a[l] = a[l],a[i]
 			permutations(a,l+1,r)
 			a[i],a[l] = a[l],a[i] #for backtracking


string = 'AAGCSDAC'
n = len(string)
a = list(string)
permutations(a,0,n-1)

