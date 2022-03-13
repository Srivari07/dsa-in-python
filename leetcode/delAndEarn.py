import collections
from typing import List


def deleteAndEarn(nums: List[int]) -> int:
    # TotalPoints=0
    # currMax=max(nums)
    # for i in range(0,len(nums)):
    #     pass
    unique_nums = collections.Counter(nums)
    prev_max, cur_max = 0, 0

    for number in range(max(unique_nums.keys())+1):
        prev_max, cur_max = cur_max, max(
            prev_max + unique_nums[number] * number, cur_max)
    return cur_max


nums = [2, 2, 3, 3, 3, 4]
print(deleteAndEarn(nums))
