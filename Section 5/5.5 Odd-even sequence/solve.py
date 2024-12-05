def is_odd(n):
    return n % 2 != 0


# def odd_even_seq(ls):
#     if len(ls) < 2:
#         return -1, None
#     low = 0
#     high = len(ls) - 1
#     while low <= high:
#         mid = (low + high ) // 2
#         if mid == low == high and is_odd(ls[mid]):
#             return -1, None
#         elif mid == 0 or is_odd(ls[mid]):
#             low = mid + 1
#         elif is_odd(ls[mid - 1]) and not is_odd(ls[mid]):
#             return mid, ls[mid]
#         else:
#             high = mid - 1

# print(*odd_even_seq(list(map(int, [input() for i in range(int(input()))]))))


# recursive version

def odd_even_seq(ls, low, high):
    mid = (low + high) // 2
    if len(ls) < 2 or low > high or (mid == low == high and is_odd(ls[mid])):
        return -1, None;
    if mid == 0 or is_odd(ls[mid]):
        return odd_even_seq(ls, mid + 1, high)
    if (is_odd(ls[mid - 1]) and not is_odd(ls[mid])) or (is_odd(ls[mid]) and not is_odd(ls[mid + 1])):
        return mid, ls[mid]
    return odd_even_seq(ls, low, mid - 1)

ls = list(map(int, [input() for i in range(int(input()))]))


print(*odd_even_seq(ls, 0, len(ls) - 1))
