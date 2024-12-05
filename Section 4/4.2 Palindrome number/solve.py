def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

# def is_palindrome(n):
#     r, m = 0, n
#     while m > 0:
#         r *= 10
#         r += m % 10
#         m //= 10
#     return n == r    

def solve(N, M):
    cnt = 0
    for num in range(N, M + 1):
        if is_palindrome(num) == True:
            cnt += 1

    return cnt


N, M = [int(num) for num in input().split()];

print(solve(N, M))