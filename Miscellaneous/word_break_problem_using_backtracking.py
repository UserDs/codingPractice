def word_break_problem(dictionary,string):
	# sentence = ""
	# n = len(string)
	# start = 0
	# while start < n:
	# 	word = ''
	# 	for i in range(start,n):
	# 		word = word + string[i]
	# 		if word in dictionary:
	# 			sentence = sentence + word +' '
	# 			start = i+1
	# 			break
	# return sentence



# dictionary = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
# string = "ilikeicecreamandmang"
dictionary = ['i','like','ice', 'cream', 'icecream']
string = 'ilikeicecream'
print(word_break_problem(dictionary,string))

