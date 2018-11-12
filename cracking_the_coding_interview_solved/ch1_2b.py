
def check(string1, string2):
        if (len(string1) != len(string2)):
            return False
        myList = [0] * 128
        for c in string1:
            ++myList[ord(c)]

        for c in string2:
            --myList[ord(c)]
            if myList[ord(c)] < 0:
                return False
        return True

string1 = input("> ")
string2 = input("> ")
print(check(string1, string2))
