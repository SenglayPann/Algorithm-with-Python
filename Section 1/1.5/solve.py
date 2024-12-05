import time


def solve(n):
    if n <= 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


n = int(input('Enter an interger:'))
start = time.time()
print('yes' if solve(n) else 'no')
end = time.time()
print(f'relapsed time : {end - start}')