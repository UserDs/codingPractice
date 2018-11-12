import math
def find_mean(list):
	return sum(list)/len(list)
def deviation(mid_list,freq_list):
	sum0 =0
	for j in range(0,len(mid_list)):
		sum0 = sum0 + mid_list[j]*freq_list[j]
	mid_list_avg = sum0/sum(freq_list)
	sum1 = 0
	n = sum(freq_list)
	for i in range (0,len(mid_list)):
		sum1 = sum1 + freq_list[i]*mid_list[i]*mid_list[i]
	num1=n*mid_list_avg*mid_list_avg
	return math.sqrt((sum1-num1)/(n))


print (deviation([4,8,11,17,20,24,32],[3,5,9,5,4,3,1]))
