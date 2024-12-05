# def anagram(ls):
#     ana_ls = []
#     for word in ls:
#         if len(ana_ls) != 0:
#             for word1 in ana_ls:
#                 if len(word) == len(word1):
#                     if ("".join(sorted(word)) == "".join(sorted(word1))):
#                         break
#                     else:
#                         ana_ls.append(word)
#         else:
#             ana_ls.append(word)
#     return ana_ls
        
# ls = [input() for _ in range(int(input()))]


# print(anagram(ls))


def anagram(n):
    ana_ls = []
    for _ in range(n):
        word = "".join(sorted(input()))
        
        if word not in ana_ls:
            print(word)
            ana_ls.append(word)

anagram(int(input()))