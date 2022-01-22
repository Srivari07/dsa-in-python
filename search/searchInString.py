s = "Srivari"
t = "v"


def fun(s, t):
    if len(s) == 0:
        return -1
    for i in range(0, len(s)-1):
        if t == s[i]:
            return i
    return -1


print(fun(s, t))
