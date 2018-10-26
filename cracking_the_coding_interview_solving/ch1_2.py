# we first sort the strings and then compare

def check(string1, string2): # function to check if two strings are permutation of each other
    if (len(string1) != len(string2)):
        return False
    if (sorted(string1) == sorted(string2)): # sorted function return a list of all characters of string in order
        return True
    else:
        return False


string1 = input("> ")
string2 = input("> ")
print(check(string1, string2))
