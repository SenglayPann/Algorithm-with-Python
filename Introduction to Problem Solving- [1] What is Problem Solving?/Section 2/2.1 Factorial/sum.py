import sys

sys.setrecursionlimit(10001)
def sum2(n, m):
    if n == m:
        return n
    return n + sum2(n + 1, m)


n, m = [int(i) for i in input('Enter an integer:').split()]
print(sum2(n, m))