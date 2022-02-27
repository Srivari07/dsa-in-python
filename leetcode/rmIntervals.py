'''
https://leetcode.com/problems/remove-covered-intervals/
'''


def removeCoveredIntervals(intervals: list[list]):
    res = 0
    last = 0
    intervals.sort(key=lambda intervals: (intervals[0], -intervals[1]))
    for _, i in intervals:
        if i > last:
            last = i
            res += 1
    return res


intervals = [[1, 2], [1, 4], [3, 4]]
print(removeCoveredIntervals(intervals))
