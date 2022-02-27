from heapq import heappush, heappop
for t in range(int(input())):
    n = input()
    a = list(map(int, input().split()))
    q = []
    ans = []
    x = 1
    for c in a:
        if c:
            heappush(q, (-c, x))
        x += 1
    while len(q) > 1:
        c, x = heappop(q)
        d, y = heappop(q)
        if c + 1:
            heappush(q, (c + 1, x))
        if d + 1:
            heappush(q, (d + 1, y))
        ans += (x, y),
    print(len(ans))
    # ans.sort(reverse=True)
    for i, j in ans:
        currMax = max(i, j)
        currMin = min(i, j)
        print(currMax, currMin)


# 4
# 2
# 2 3
# 3
# 1 2 3
# 3
# 0 0 2
# 4
# 1 2 3 4
