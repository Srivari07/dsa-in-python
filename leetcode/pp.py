'''
https://leetcode.com/problems/palindrome-partitioning/
'''


from typing import List


def partition(s: str) -> List[List[str]]:
    answer = []
    up = ""
    res = []
    helper(s, up, answer, res)
    answer.append(res)
    return answer


def helper(s, up, answer, res: list):
    if len(s) == 0:
        res.append(up)
        return
    ch = s[0]
    helper(s[1:], up, answer, res)
    helper(s[1:], up+ch, answer, res)


s = "abba"
print(partition(s))
