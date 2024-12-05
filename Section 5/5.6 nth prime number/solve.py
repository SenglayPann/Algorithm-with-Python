
def find_prime(n):
    sieve = [0, 0] + [1] * (n - 1)
    for i in range(2, int(n ** .5 ) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    return [i for i in range(n) if sieve[i] == 1]

def bi_search(x, ls):
    low, high = 0, len(ls) - 1
    while low <= high:
        mid = (low + high) // 2
        if ls[mid] == x:
            return mid
        elif ls[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return - 1

def solve(ls):
    primes = find_prime(max(ls))
    for num in ls:
        print(bi_search(num, primes) + 1, end = ' ')


solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])