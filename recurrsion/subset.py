from typing import List

nums = [1, 2, 2]


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    helper(nums, [], res)
    return res


def helper(nums, path, res):
    res.append(path)
    for i in range(0, len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        helper(nums[i+1:], path+[nums[i]], res)


print(subsets(nums))
