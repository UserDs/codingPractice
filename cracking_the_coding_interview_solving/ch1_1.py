# In this method we use a list to store the charecters as we iterate the string
# import time
# start = time.time()

def check_unique(string):
    list = []
    list.append(string[0])
    n = len(string)
    for i in range (1, n):
        if string[i] in list:
            print("Not unique")
            break
        else:
            list.append(string[i])

        if i == n - 1:
            print("unique")
# check_unique("tryk7jrhegwf")
# check_unique("tryk7j")
string = input('> ')
check_unique(string)

# end = time.time()
# print(end - start)
