def solve(S, N):
    maxn, maxi = S[0], 0
    for i in range(1, N):
        if S[i] > maxn : 
            maxn  = S[i]
            maxi = i
    return maxn, maxi

S = [int(n) for n in input('Enter a list of integers sperarate by space:').split()]
N = len(S)

print(solve(S, N))