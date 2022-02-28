t = int(input())
while t > 0:
    s = int(input())
    arr = list(map(int, input().split()))[:s]
    n = len(arr)
    hashmap = dict()
    for i in range(n):
        if arr[i] in hashmap.keys():
            hashmap[arr[i]] += 1
        else:
            hashmap[arr[i]] = 1

    max_count = 0
    res = -1
    for i in hashmap:
        if (max_count < hashmap[i]):
            res = i
            max_count = hashmap[i]

    print(res)
    t -= 1
