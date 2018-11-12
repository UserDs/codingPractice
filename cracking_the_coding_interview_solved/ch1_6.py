def counting(string, i):
    string = string + "1"
    count = 1
    j = i + 1
    while string[i] == string[j]:
        count = count + 1
        j = j + 1
    return count

def array(string):
    sum = counting(string, 0, 1)
    list = []
    list.append(sum)
    while sum != len(string):
        sum = sum + counting(string, sum, sum + 1)
        list.append(sum)
    return list

def compress(string):
    string1 = ""
    list1 = array(string)
    n = len(list1)
    string1 = string1 + string[list1[0]-1] + f"{list1[0]}"
    for i in range(1, n):
        string1 = string1 + f"{string[list1[i]-1]}{list1[i] - list1[i-1]}"
    if len(string1) > len(string):
        return string
    else:
        return string1


string = input("> ")
print(counting(string, 0, 1))
print(array(string))
print(compress(string))
