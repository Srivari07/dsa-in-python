

# even odd
'''
a = 72813791837
if a & 1 == 1:
    print("odd")
else:
    print("even")
'''

# occurance of no. in array less than twice
'''
arr = [1, 1, 2, 2, 3, 4, 4, 5, 5]
u = 0
for i in arr:
    u = u ^ i
print(u)
'''

# find the ith bit of a no
# https://stackoverflow.com/questions/10493411/what-is-bit-masking
'''
a = 14
i = 3
ans = ((a & (1 << (i-1))) >> (i-1))
print(ans)
'''
# https://www.geeksforgeeks.org/find-the-element-that-appears-once/

'''
from typing import Counter
arr = [2, 2, 3, 2, 7, 7, 8, 7, 8, 8]
f = Counter(arr)
for i in f:
    if (f[i] == 1):
        print(i)

'''
# find the nth magic no.
'''
n = 7
ans = 0
base = 5
while n > 0:
    last = n & 1
    n = n >> 1
    ans = ans+last*base
    base = base*5

print(ans)
'''

# no. of digits in a binary no.

import math
n = 7
base = 2
b = bin(7)
print(b)
d = int(math.log2(7)+1)
print(d)
