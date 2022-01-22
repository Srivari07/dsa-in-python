
# s = 'abc'
# ans = ['a', 'b', 'c', 'ab', 'bc', 'ca', 'abc']
# pattern in subset of taking some element and removing some element

# def fun(p, up):
#     if len(up) == 0:
#         print(p, end=' ')
#         return
#     ch = up[0]
#     fun(p+ch, up[1:])
#     fun(p, up[1:])

# fun(p='', up='abc')


# def fun(p, up):

#     if len(up) == 0:
#         list = []
#         list.append(p)
#         return list
#     ch = up[0]
#     left = []
#     right = []
#     left = fun(p+ch, up[1:])
#     right = fun(p, up[1:])
#     left = left+right
#     return left


# print(fun(p='', up='abc'))

# def fun(p, up):
#     if len(up) == 0:
#         print(p, end=' ')
#         return
#     ch = up[0]
#     fun(p+ch, up[1:])
#     fun(p, up[1:])


# fun(p='', up='abbc')


# subset
l = [1, 2, 3]


def fun(l):
    outer = [[]]
    for i in range(len(l)+1):
        for j in range(i):
            outer.append(l[j:i])
    return outer


print(fun(l))
