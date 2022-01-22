
# HCF
# by euclidean algorithm
# gcd(a,b)=gcd(b%a,a)
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


a = 4
b = 8
print(gcd(a, b))
