def i_sort(ls):
    cnt = 0
    for i in range(1, len(ls)):
        j, val = i - 1, ls[i]
        cnt += 1
        while j >= 0 and ls[j] > val:
            ls[j + 1] = ls[j]
            j -= 1
            cnt += 1
        ls[j + 1] = val
    return cnt

print(i_sort(list(map(int, [input() for _ in range(int(input("Enter number of element")))]))))