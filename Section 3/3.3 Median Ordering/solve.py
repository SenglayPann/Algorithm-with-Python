def median(ls):
    ls.sort()
    while len(ls) >= 1:
        mid = (len(ls) -1 ) // 2
        print(ls[mid], end = " ")
        ls.remove(ls[mid])


ls = [int(num) for num in input().split()]

median(ls)