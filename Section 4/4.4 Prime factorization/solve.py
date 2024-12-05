def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(False)
            return False
    print(True)
    return True

# def pf(n):
#     if n < 2:
#         return []
#     else:
#         for i in range(2, int(n ** .5) + 1):
#             if n % i == 0:
#                 return [i] + pf(n // i)
#         return [n]

# def pf(n, m):
#     if n < 2:
#         return []
#     elif m > int(n ** .5):
#         return [n]
#     elif n % m == 0:
#         return [m] + pf(n // m, m)
#     else:
#         return pf(n, m + 1)

# print(pf(210, 2))



def pf(n):
    factors = []
    for i in range(2, int(n ** .5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n != 1:
        factors.append(n)
    return factors

print(pf(10))