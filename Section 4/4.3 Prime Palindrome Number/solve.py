import time

def pp(N, M):
    cnt = 0
    for num in range(N, M + 1):
        if num < 11:
            continue
        if str(num) == str(num)[::-1]:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                cnt += 1

    return cnt
N, M = map(int, input().split())

start = time.time()

print(pp(N, M))

end = time.time()

print("Execution time: ", end - start)