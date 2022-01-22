

n = 40
p = 3

# T(n)=O(log n)


def sqrt(n, p):
    start = 0
    end = n
    root = 0.0

    while(start <= end):
        mid = start+(end-start)//2

        if mid * mid == n:
            root = mid
            return root
        if mid*mid > n:
            end = mid-1
        else:
            start = mid+1

    incr = 0.1
    for i in range(0, p):
        while root * root <= n:
            root += incr
        root -= incr
        incr /= 10
    return root


print(sqrt(n, p))
