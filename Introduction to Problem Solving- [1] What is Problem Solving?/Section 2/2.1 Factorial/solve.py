
## recursion 
# import sys
# import time

# sys.setrecursionlimit(10 ** 5 + 1)
# def solve(n):
#     if n < 0:
#         return -1
#     if n == 1 or n == 0:
#         return 1
#     return n * solve(n - 1)

# start = time.time()
# n = int(input('Enter an integer:'))
# print(solve(n))
# end = time.time()

# print(end - start)


## iteration

def solve(n):
    if n == 0 or n == 1:
        return 1
    s = 1
    for i in range(n, 0, -1):
        s *= i
    return s

n = int(input('Enter an integer:'))
print(solve(n))