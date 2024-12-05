def Bitonic(ls) :
    if len(ls) < 2:
        return -1, None
    low = 0
    high = len(ls) - 1
    while low <= high :
        mid =  (low +  high) // 2
        if mid == 0:
            if ls[mid] > ls[mid - 1]:
                return mid, ls[mid]
            else:
                return mid + 1, ls[mid + 1] 
        elif mid == len(ls) - 1:
            if ls[mid] > ls[mid - 1]:
                return mid, ls[mid]
            else:
                return mid -1, ls[mid - 1]
        elif ls[mid - 1] < ls[mid] > ls[mid + 1] or low == high :
            return mid, ls[mid]
        elif ls[mid - 1] < ls[mid] < ls[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

print(*Bitonic(list(map(int, [input() for i in range(int(input()))]))))