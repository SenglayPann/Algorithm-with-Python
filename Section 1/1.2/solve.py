def solve(N):
    # s = 0
    # for i in range(1, N + 1):
    #     s += i
    # return s
    return N * (N + 1) // 2
    

N = int(input())
print(solve(N))