
'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''


from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort(key=lambda x: x[1])
    n, count = len(points), 1
    if n == 0:
        return 0
    curr = points[0]

    for i in range(n):
        if curr[1] < points[i][0]:
            count += 1
            curr = points[i]

    return count


points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots(points))
