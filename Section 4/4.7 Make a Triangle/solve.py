# def traingle(n):
#     traingle_side_length = []
#     for i in range(1, int(n ** .5) + 1):
#         if n % i == 0:
#             traingle_side_length.append(i)
#             traingle_side_length.append(n // i)
#             n //= i
#             traingle_side_length.append(n)
            
#     return traingle_side_length


# print(traingle(3))


# def traingle(n):
#     cnt = 0
#     for a in range(1, n):
#         for b in range(a, n):
#             for c in range(b, n):
#                 if a + b + c == n  and a + b > c:
#                     cnt += 1
#     return cnt



# print(traingle(6))


# improve solution 

# def traingle(n):
#     iter = 0
#     for a in range(1, n - 1):
#     cnt = 0
#         for b in range(a, n - 1):
#             c = n - (a + b)
#             iter += 1
#             if b <= c and c < a + b:
#                 cnt += 1
#     print(iter)
#     return cnt

# print(traingle(6))


# def traingle(n):
#     cnt = 0
#     for c in range((n + 1) // 3, (n + 1) // 2):
#         for b in range((n - c + 1) // 2, c + 1):
#             cnt += 1
#             print(c, b, n - c - b)
#     return cnt


# print('Number of triangles that can be created:', traingle(10))


# def traingle(n):
#     cnt = 0
#     for c in range((n + 1) // 3, (n + 1) // 2):
#         b_range = c + 1 - (n - c + 1) // 2
#         cnt += b_range
#     return cnt

# print(traingle(9))


def traingle_recursive(n, c_start=None, b_start=None, cnt=0):
    if c_start is None:
        c_start = (n + 1) // 3
    if b_start is None:
        b_start = (n - c_start + 1) // 2

    if c_start >= (n + 1) // 2:
        return cnt

    if b_start > c_start:
        return traingle_recursive(n, c_start + 1, (n - c_start - 1) // 2, cnt)

    cnt += 1
    print(c_start, b_start, n - c_start - b_start)

    return traingle_recursive(n, c_start, b_start + 1, cnt)

print('Number of triangles that can be created:', traingle_recursive(10))