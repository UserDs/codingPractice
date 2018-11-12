def total_ways(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return total_ways(n-1) + total_ways(n-2) + total_ways(n-3)
n = int(input("> "))
print(total_ways(n))
