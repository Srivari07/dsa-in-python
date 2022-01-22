
def combinationSum2(self, arr, target):
    arr.sort()
    result = []
    helperFun(arr, target, 0, result, [])
    return result


def helperFun(arr, t, start, result, path):
    if t < 0:
        return
    if t == 0:
        result.append(path)
    for i in range(start, len(arr)-1):
        if i > start and arr[i] == arr[i-1]:
            continue
        helperFun(arr, t-arr[i], i+1, result, path+[arr[i]])
