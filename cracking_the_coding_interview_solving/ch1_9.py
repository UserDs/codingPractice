def isSubstring(s1, s2):
    if s1.find(s2) == -1:
        return False
    else:
        return True

def isRotation(s1, s2):
    for i in range(0, len(s1)):
        if isSubstring(s1[i:] + s1[:i], s2) is True:
            return "Yes"
    return "No"


s1 = input("> ")
s2 = input("> ")
print(isRotation(s1, s2))
