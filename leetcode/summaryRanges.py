def summaryRanges(nums):
    if not nums:
        return
    start = -1
    res = []
    for i in range(1, len(nums)):
        if nums[i]-nums[i-1] == 1 and start == -1:
            start = nums[i-1]
        if nums[i]-nums[i-1] != 1:
            if start == -1:
                res.append(str(nums[i-1]))
            else:
                res.append(str(start)+'->'+str(nums[i-1]))
                start = -1
    if start == -1:
        res.append(str(nums[-1]))
    else:
        res.append(str(start)+'->'+str(nums[-1]))
    return res


nums = []
print(summaryRanges(nums))
