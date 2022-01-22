

# see notes

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def lcm(a, b):
    LCM = (a*b)//(gcd(a, b))
    return LCM


a = 3
b = 7
print(lcm(a, b))
