def toString(list): # ['a', 'b', 'c'] => 'abc'
	return ''.join(list)


def uniqe_permutations(a,l,r):
	if l == r:
		print toString(a)
	else:
		list = []  #storing to avoid repeatation
 		for i in range(l,r+1):
			#print i,l,a[i],a[l]
			if a[i] not in list:
				a[i],a[l] = a[l],a[i]
				uniqe_permutations(a,l+1,r)
				a[i],a[l] = a[l],a[i] #for backtracking
			list.append(a[i])

string = 'ABCA'
n = len(string)
a = list(string)
uniqe_permutations(a,0,n-1)