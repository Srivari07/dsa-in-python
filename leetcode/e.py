t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    count = 0
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if (arr[i] ^ arr[j]) % 3 == 0 and (arr[i]+arr[j]) % 3 == 0:
                count += 1
    print(count)
