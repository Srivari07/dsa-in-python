from math import sqrt

t = int(input())
for _ in range(t):
    n = int(input())

    def countSetBit(n):
        c = 0
        while n:
            c += n & 1
            n >>= 1
        return c

    def isPrime(N):
        k = int(sqrt(N)) + 1
        for i in range(2, k, 1):
            if (N % i == 0):
                return False

        return True

    def getDifference(N):
        if (N == 0):
            return 2
        elif (N == 1):
            return 1
        elif (isPrime(N)):
            return 0
        floorN = -1
        n1 = N - 1
        while (True):
            if (isPrime(n1)):
                floorN = n1
                break

            else:
                n1 -= 1
        return floorN

    psd = countSetBit(n)-countSetBit(getDifference(n))
    print(psd, countSetBit(n), countSetBit(getDifference(n)))
    # if psd > 0:
    #     print("PRIME LOSES")
    # elif psd == 0:
    #     print("PRIME EQUALS")
    # else:
    #     print("PRIME WINS")
