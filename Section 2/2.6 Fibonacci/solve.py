# def fibonacci(n) :
#     if n == 1 or n == 2:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)


# for i in range(10):
#     print(fibonacci(i))


# Improved solution 

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else :
        a, b = 1, 1
        for i in range(3, n + 1):
            a, b = b, a + b
    return b

# for i in range(1, 29 + 1):
#     print(fibonacci(i), end = ' ')

print(fibonacci(20))
