def b_sort(ls):
    count = 0
    for i in range(len(ls) - 1, 0, -1 ):
        for j in range(i):
            if ls[j + 1] < ls[j]:
                ls[j + 1], ls[j] = ls[j], ls[j + 1]
                count += 1
    return count


print(b_sort([int(input()) for _ in range(int(input('Enter the len of the number list:')))]))