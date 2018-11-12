import time
start = time.time()

def kth_non_repeating(string,k):
	n=len(string)
	count = 0
	for i in range(0,n):
		p=0
		for j in range(0,n):
			if j != i:
				if string[i] == string[j]:
					p=1
					break
		if p == 0:
			count = count+1
		if count == k:
			return string[i]
string = 'therearealotofproblemsinthisworldwhichwecansolve'
k=5
print(kth_non_repeating(string,k))

end = time.time()
print(end - start)
