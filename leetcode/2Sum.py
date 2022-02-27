def twoSum(nums, target):
    d = {}
    for i, value in enumerate(nums):
        remain = target-value

        if remain in d:
            # return [i, d[remain]]
            return [d[remain]+1, i+1]
        else:
            d[value] = i


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))
