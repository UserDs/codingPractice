def how_many_between(list,x,y):
	total = 0
	for i in range(0,len(list)):
		if list[i]>=x and list[i]<=y:
			total = total+1
	return total

print(how_many_between([-1,0,0,2,3,4,2,5,6,4,3,],2,5))

