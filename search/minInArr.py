
arr = [18, 12, -7, 3, 14, 28]


def fun(arr):
    ans = arr[0]
    for i in range(0, len(arr)-1):
        if(arr[i] < ans):
            ans = arr[i]

    return ans


print(fun(arr))
