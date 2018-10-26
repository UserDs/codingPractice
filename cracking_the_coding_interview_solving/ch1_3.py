
def check(string, true_length):
    desired_string = ""
    for i in range(true_length):
        if string[i] == ' ':
            desired_string = desired_string + "%20"
            continue
        desired_string = desired_string + string[i]
    return desired_string

string = input("> ")
true_length = int(input("> "))
print(check(string, true_length))
