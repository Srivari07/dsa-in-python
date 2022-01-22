from math import sqrt


def fiboFormula(n):
    return (int)(pow(((1+sqrt(5))/2), n)/sqrt(5))


def fibo(n):
    if n < 2:
        return n
    return fibo(n-1)+fibo(n-2)


# for i in range(0, 10):
#     print(fiboFormula(i))

print(fiboFormula(50))
# print(fibo(n))
