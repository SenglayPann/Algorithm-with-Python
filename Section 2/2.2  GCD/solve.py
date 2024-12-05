# def gcd(n, m):
#     if n < m:
#         n, m = m, n
#     if m == 0:
#         return n
#     return gcd(m, n % m)

# n, m = [int(i) for i in input('Enter two integers:').split()]
# print(gcd(n, m))


## improved solution: through iteration

def gcd(n, m) : 
    if n < m :
        n, m = m, n
    while m != 0 :
        n, m = m, n % m
    return n

n, m = [int(i) for i in input('Enter two integers:').split()]
print(gcd(n, m))
