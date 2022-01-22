

n = 23597
res = 0
while n > 0:
    last_digit = n % 10
    n = n//10
    res = (res*10)+last_digit
print(res)
