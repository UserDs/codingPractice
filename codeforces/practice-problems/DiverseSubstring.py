n = int(input())
given_string = input()
dummy = 0
for i in range(0, n-1):
    if given_string[i] != given_string[i+1]:
        print("YES")
        print(given_string[i:i+2])
        dummy = 1
        break
if dummy == 0:
	print("NO")

