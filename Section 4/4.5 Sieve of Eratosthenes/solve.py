# def find_prime(n):
#     sieve = [0, 0] + [1] * (n - 1)
#     for i in range(2, n + 1):
#         if sieve[i] == 1:
#             for j in range(i + i, n + 1, i):
#                 sieve[j] = 0
#     return sieve


# print(sum(find_prime(100)))


# improved solution
def find_prime(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return sieve


print(sum(find_prime(100)))