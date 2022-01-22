
'''
n = 20
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")
'''

import math
n = 20
for i in range(1, round(math.sqrt(n+1))):
    if n % i == 0:
        if n//i == i:
            print(i, end=" ")
        else:
            print(f"{i} {n//i}", end=" ")
