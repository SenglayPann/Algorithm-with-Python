# accending order

# def co_sort(co_ls):
#     return sorted(co_ls, key = lambda k : (k[0], k[1]))



# N = int(input('Enter number of pairs of coordinate:'))
# co_ls = []
# for i in range(N):
#     co_ls.append(tuple([int(num) for num in input().split()]))

# print(co_sort(co_ls))

# decending order

def co_sort(co_ls):
    return sorted(co_ls, key = lambda k : (k[0], -k[1]), reverse = True) # -k mean in deccending order




co_ls = [tuple([int(num) for num in input().split()]) for _ in range(int(input('Enter number of pairs of coordinate:')))]

print(co_sort(co_ls))