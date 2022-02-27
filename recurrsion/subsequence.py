
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
arr = [1, 2, 3]


def fun(arr):
    outer = [[]]
    for i in sorted(arr):
        outer += [j+[i] for j in outer]
    return outer


print(fun(arr))
