num = int(input())

if num > 1:
	for i in range(2, num):
		if num % i == 0:
			print("No")
	
	# this else will execute only if the index i in loop fail to be in the range (2, num)
	else:
		print("Yes")

else:
	print("No")



