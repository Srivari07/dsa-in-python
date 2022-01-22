n = 1385757879
c = 0
while n > 0:
    rem = n % 10
    if rem == 7:
        c += 1
    n = n//10

print(c)
