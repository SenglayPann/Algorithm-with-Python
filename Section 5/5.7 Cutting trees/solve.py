def cutting_tree(ls, M):
    low, high = min(ls), max(ls)
    total = 0
    while low <= high and total >= M:
        mid = (low + high) // 2
        if 