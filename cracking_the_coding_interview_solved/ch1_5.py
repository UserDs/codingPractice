
def one_way(string1, string2):
    n1 = len(string1)
    n2 = len(string2)
    if string1 == string2:
        return True

    if abs(n1 - n2) > 1:
        return False

    if n1 == n2:
        for i in range(0, n1):
            if string1[i] != string2[i]:
                if string1[0:i]+string1[i+1:n1] == string2[0:i]+string2[i+1:n1]:
                    return True
                else:
                    return False

    if n1 > n2:
        for i in range(0, n2):
            if string1[0:n2] == string2[0:n2]:
                return True
            if string1[i] != string2[i]:
                if (string1[0:i] + string1[i+1:n1]) == string2:
                    return True
                else:
                    return False

    if n2 > n1:
        for i in range(0, n1):
            if string1[0:n1] == string2[0:n1]:
                return True
            if string1[i] != string2[i]:
                if (string1[0:i] + string1[i+1:n2]) == string2:
                    return True
                else:
                    return False

string1 = input("> ")
string2 = input("> ")
print(one_way(string1, string2))
