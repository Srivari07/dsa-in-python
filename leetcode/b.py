t = int(input())
while t > 0:
    n = int(input())

    def isComposite(n):
        if (n <= 1):
            return False
        if (n <= 3):
            return False
        if (n % 2 == 0 or n % 3 == 0):
            return True
        i = 5
        while(i * i <= n):
            if (n % i == 0 or n % (i + 2) == 0):
                return True
            i = i + 6
        return False

    def isPrime(n):
        if n > 1:
            for i in range(2, int(n/2)+1):
                if (n % i) == 0:
                    return False
                    break
            else:
                return True
        else:
            return False

    if isComposite(n) == True and isPrime(n) == True:
        for num in range(2, n + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)

    t -= 1
