t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    res = 0
    i = 0
    j = len(arr)-1
    while i < j:
        res = max(res, (j-i)*min(arr[i], arr[j]))
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    print(res)
