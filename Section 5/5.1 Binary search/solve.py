# def bi_search(ls, x, high, low = 0):
#     if low > high:
#         return -1
#     mid = (low + high) // 2
#     if ls[mid] == x:
#         return mid
#     if ls[mid] > x:
#         return bi_search(ls, x, mid - 1, low)
#     if ls [mid] < x:
#         return bi_search(ls, x, high, mid + 1 )
    


# S, X = [list(map(int,input().split())) for _ in range(2)]

# S.sort()

# for num in X:
#     print(bi_search(S, num, len(S)), end = ' ')



# solution 2

def bisearch(s, n):
    low = 0
    high = len(s) - 1
    while low <= high:
        mid = (low + high) // 2
        if s[mid] > n:
            high = mid - 1
        elif s[mid] < n:
            low = mid + 1
        else:
            return mid
    return -1

S, X = [list(map(int,input().split())) for _ in range(2)]

S.sort()

for num in X:
    print(bisearch(S, num), end = ' ')

    