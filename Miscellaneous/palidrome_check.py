def is_palidrome(word):
	for i in range(0,len(word)/2):
		if word[i] == word[len(word)-1-i]:
			return "Yes"
	return "No"
print(is_palidrome('deepak'))
print(is_palidrome('malyalam'))
print(is_palidrome(''))
print(is_palidrome('deed'))
print(is_palidrome('3333'))
t