

'''
https://leetcode.com/problems/merge-intervals/
'''


def mergeInterval(intervals):
    intervals.sort()
    ans = []
    for i in intervals:
        if not ans or ans[-1][1] < i[0]:
            ans.append(i)
        else:
            ans[-1][1] = max(ans[-1][1], i[1])

    return ans


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeInterval(intervals))
