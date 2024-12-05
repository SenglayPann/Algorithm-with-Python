def solve(ls):
    odd = []
    even = []
    for num in ls:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    print(*sorted(odd))
    print(*sorted(even, reverse = True))


solve([int(num) for num in input().split()])