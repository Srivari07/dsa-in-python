'''
n = 8
for i in range(2, n):
    if n % i == 0:
        print(f"{n} Not prime ")

else:
    print(f"{n} is prime")
'''


def isPrime(n):
    if n <= 1:
        return False

    c = 2
    while c*c <= n:  # i.e. c <= sqrt(n)
        if n % c == 0:
            return False
        c += 1
    return True


n = 36
for i in range(1, n):
    print(f"{i} {isPrime(i)}")
