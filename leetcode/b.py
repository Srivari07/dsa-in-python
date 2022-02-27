t = int(input())
for _ in range(t):
    n = list(map(str, input().split()))
    s = list(map(int, input().split()))
    r = list(map(int, input().split()))
    total = [s[i]+r[i] for i in range(len(s))]
    m = dict(zip(n, total))
    d = dict(zip(n, s))
    d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    currMax = max(m, key=m.get)
    for i, k in enumerate(d):
        if currMax == k:
            print(k, i)

# 2
# Hari Hara Sudhan Thevar
# 86 1 72 18
# 79 45 4 57
# Hari Hara Sudhan Thevar
# 63 45 42 54
# 11 31 61 83
