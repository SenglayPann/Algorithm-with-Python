# def collatz(n, seq = []):
#     if n < 1 :
#         return None, None
#     if n == 1 :
#         seq.append(n)
#         return len(seq), seq
#     if n % 2 == 0:
#         seq.append(n)
#         return collatz(n // 2, seq)
#     else :
#         seq.append(n)
#         return collatz(3 * n + 1, seq)

# n = int(input('Enter an integer:'))
# l , seq = collatz(n)


# print(l)
# print(*seq)


def collatz(n):
    if n < 1:
        return []
    if n == 1 :
        return [n]
    elif n % 2 == 0:
        return [n] + collatz(n // 2)
    return [n] + collatz(3 * n + 1)

n = int(input('Enter an integer:'))
seq = collatz(n)
print(len(seq))
print(*seq)