# import time

# def solve(N) :
#     count = 0
#     for i in range(1, N + 1):
#         if N % i == 0:
#             count += 1
#     return count

# start = time.time();
# N = int(input('Enter N:'))
# end = time.time()
# print(solve(N), 'in', end - start, 'second')


# ## solution 2


# import math as m

# def solve(n):
#     ## find all divisors
#     count = 0
#     for i in range(1, m.ceil(m.sqrt(n)) + 1):
#         if n % i == 0:
#             count += 1
#     count *= 2
#     ## n is a perfect square
#     if m.sqrt(n) == m.ceil(m.sqrt(n)) :
#         count -= 1
#     return count

# print(solve(1234567890))


import math as m

def solve(n):
    ## find all divisors
    divisors = []
    for i in range(1, m.ceil(m.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    
    ## n is a perfect square
    if m.sqrt(n) == m.ceil(m.sqrt(n)) :
        divisors.remove(m.sqrt(n))
    return sum(divisors)

print(solve(1234567890))