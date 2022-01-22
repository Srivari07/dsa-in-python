

# https://leetcode.com/problems/largest-divisible-subset/submissions/


def largestDivisibleSubset(nums):
    n = len(nums)
    if n == 0:
        return []
    nums = sorted(nums)
    dp = [[nums[i]] for i in range(n)]
    answer = [nums[0]]
    for i in range(1, n):
        for j in range(0, i):
            if nums[i] % nums[j] == 0:
                t = dp[j] + [nums[i]]
                if len(t) > len(dp[i]):
                    dp[i] = list(t)
                if len(dp[i]) > len(answer):
                    answer = dp[i]
    return answer


nums = [1, 2, 3]
print(largestDivisibleSubset(nums))
