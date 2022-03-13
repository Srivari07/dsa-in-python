def countBits(n):
    ans = []
    for i in range(0, n+1):
        j = countSetBits(i)
        ans.append(j)
    return ans


def countSetBits(i):
    count = 0
    while i:
        i &= (i-1)
        count += 1

    return count


n = 15
print(countBits(n))
