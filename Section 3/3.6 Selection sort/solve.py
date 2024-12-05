def s_sort(ls):
    count = 0
    for i in range(len(ls) -1):
        min = i
        for j in range(i,  len(ls) - 1):
            if ls[j+ 1] < ls[min]:
                min = j + 1
        if min != i:
            ls[min],ls[i] = ls[i], ls[min]
            count += 1
    return count

print(s_sort([int(input()) for _ in range(int(input('Enter the len of the number list:')))]))