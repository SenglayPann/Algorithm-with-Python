# def bisearch(n, s):
#     low = 0
#     high = len(s) - 1
#     cnt = 0 
#     while low <= high:
#         cnt += 1
#         mid = (low + high) // 2
#         if s[mid] == n:
#             return cnt + 1
#         elif s[mid] < n:
#             high = mid - 1
#         elif s[mid] > n:
#             low = mid + 1
#     return cnt


# s, x = [list(map(int, input().split())) for _ in range(2)]

# s.sort()
# total = 0
# for num in x:
#     total += bisearch(num, s)
# print(total)

# recursion function

def bisearch(low, high, n, s):
    if low > high:
        return 0
    mid = (low + high) // 2
    if s[mid] == n:
        return 1
    if s[mid] < n:
        return bisearch(low, mid - 1, n, s) + 1
    if s[mid] > n:
        return bisearch(mid + 1, high, n, s) + 1
    

s, x = [list(map(int, input().split())) for _ in range(2)]

s.sort()
total = 0
for num in x:
    total += bisearch(0, len(s) - 1, num, s)
print(total)