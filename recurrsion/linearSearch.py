
'''
arr = [1, 2, 8, 4, 5, 8, 6, 7]

res = []


def search(arr, t, i):
    global res
    if i == len(arr):
        return -1
    if arr[i] == t:
        res.append(i)
    search(arr, t, i+1)


search(arr, 8, 0)
print(res)
'''

# this one
'''
def search(arr, t, i, res):
    if i == len(arr):
        return res
    if arr[i] == t:
        res.append(i)
    return search(arr, t, i+1, res)


arr = [1, 2, 8, 4, 5, 8, 6, 7]
res = []
print(search(arr, 8, 0, res))
print(res)
'''


def search(arr, t, i):
    res = []
    if i == len(arr):
        return res
    if arr[i] == t:
        res.append(i)
    ansFromBelowCalls = search(arr, t, i+1)
    res.extend(ansFromBelowCalls)
    return res


arr = [1, 2, 8, 4, 5, 8, 6, 7]
print(search(arr, 8, 0))

# this is not a optimal approach because at each function call we create new list ,hence use above apporach.
