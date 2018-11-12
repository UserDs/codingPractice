import time
start = time.time()

import collections
def kth_nonrepeating(word,k):
	n = len(word)
	mydict = collections.OrderedDict()
	for i in range(0,n):
		if mydict.has_key(word[i]) == False:
			mydict[word[i]] = 1
		else:
			mydict[word[i]] = mydict[word[i]]+1
	count = 0
	for key in mydict:
		if mydict[key] == 1:
			count = count+1
		if count == k:
			return key

word = 'therearealotofproblemsinthisworldwhichwecansolve'
k = 5
print(kth_nonrepeating(word,k))

end = time.time()
print(end - start)
