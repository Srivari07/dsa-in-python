t = int(input())
for _ in range(t):
    s = str(input())
    getVals = list([val for val in s if val.isalpha() or val == " "])
    ns = "".join(getVals)
    print(ns[::-1])
