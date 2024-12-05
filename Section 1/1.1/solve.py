# Matrices addition function
def madd(A, B):
    n, m = len(A), len(A[0])
    C = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

# Print matrix function
def mprint(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end = ' ')
        print()

# User input  Matrices
N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = madd(A, B)
mprint(C)