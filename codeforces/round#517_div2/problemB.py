# import math
# def number(b):
#     count = 0
#     for i in range(1, int(math.sqrt(b))+1):
#         if (b % i == 0):
#             count = count + 1
#     if (math.sqrt(b).is_integer() == True ):
#         return 2 * count - 1
#     else:
#         return 2 * count
# b = int(input())
# print(number(b))

import math
b = int(input())
count = 0
for i in range(1, int(math.sqrt(b))+1):
    if (b % i == 0):
        count = count + 1
if (math.sqrt(b).is_integer() == True ):
    print(2 * count - 1)
else:
    print(2 * count)
