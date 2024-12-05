import random as rd

# def TQG(s, t, x):
#     low = 0
#     high = t
    
#     while low < high:
#         print(low, high, end=' ')
#         mid = (low + high) // 2
#         print('Bigger than {}?'.format(mid), end=' ')
#         if x > mid:
#             print('yes')
#             low = mid + 1
#         else:
#             print('no')
#             high = mid
#     print('The number is:', low)

def TQG(low, high, x):
    if low > high:
        print('Invalid')
        return
    if low == high:
        print('The number is {}'.format(low))
        return
    else:
        print(low, high, end=' ')
        mid = (low + high) // 2
        print('Bigger than {}'.format(mid), end=' ')
        if x > mid :
            print('yes')
            return (TQG(mid + 1, high, x))
        else:
            print('no')
            return TQG(low, mid, x)
s, t = map(int, input().split())

SEED = int(input())
rd.seed(SEED)
x = rd.randint(s, t)
print(x)
TQG(s, t, x)


