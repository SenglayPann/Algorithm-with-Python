# import copy 
# def solve(n):
#     def generateAplha(n):
#         return [chr(ord('A') + i) for i in range(n)]

#     def permutation(s, n = 0):
        
#         if len(s) - n == 1:
#             print(''.join(s))
#         s1 = copy.deepcopy(s)
#         for i in range (n, len(s1)):
#             s1[n], s1[i] = s1[i], s1[n]
#             permutation(s1, n + 1)

#     s = generateAplha(n)
#     permutation(s)

# solve(8)


## solution 

def perm(s, m = 0):
    if len(s) - m == 1:
        print(''.join(s))
    else :
        for i in range(m, len(s)):
            s[m], s[i] = s[i], s[m]
            perm(s, m + 1)
            s[m], s[i] = s[i], s[m]

n = int(input('enter an integer:'))

s = [chr(ord('A') + i) for i in range(n)]

perm(s)