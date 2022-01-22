

'''
https://leetcode.com/problems/happy-number/
'''


def isHappy(n: int) -> bool:
    slow = n
    fast = n
    while fast != slow:
        slow = findSquare(slow)
        fast = findSquare(findSquare(fast))
    if slow == 1:
        return True
    return False


def findSquare(n):
    ans = 0
    while n > 0:
        rem = n % 10
        n = n//10
        ans = ans+rem*rem
    return ans
