# t = int(input())
# while(t > 0):
#     n = int(input())
#     given_sequence = list(map(int, input().split()))
#     dummy = 0
#     for i in range(0, n- 1):
#         for j in range(i+1, n):
#             if given_sequence[i] == given_sequence[j]:
#                 if (i + 1 in given_sequence and j + 1 in given_sequence) == True:
#                     print("Truly Happy")
#                     dummy = 1
#                     break
#         if dummy == 1:
#             break
#     if dummy == 0:
#         print("Poor Chef")
#     t = t - 1

t = int(input())
while(t > 0):
    n = int(input())
    given_sequence = list(map(int, input().split()))
    dummy = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if given_sequence[i] != given_sequence[j]:
                if given_sequence[given_sequence[i] - 1] == given_sequence[given_sequence[j] - 1]:
                    print("Truly Happy")
                    dummy = 1
                    break
        if dummy == 1:
            break
    if dummy == 0:
        print("Poor Chef")
    t = t - 1
