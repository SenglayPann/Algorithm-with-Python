def seqsearch(x, S):
    for i in range(len(S)):
        if S[i] == x:
            return i
    return -1


S, N = [[int(num) for num in input().split()] for _ in range(2)]

for num in N:
    print(seqsearch(num, S), end=" ")