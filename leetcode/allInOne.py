'''
https://leetcode.com/problems/permutations/
'''


from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        self.helper(nums, answer, tempAns=[])
        return answer

    def helper(self, nums: List[int], answer: List[int], tempAns: List[int]):
        if len(nums) == len(tempAns):
            answer.append(tempAns)
        else:
            for i in range(0, len(nums)):
                if nums[i] in tempAns:
                    continue
                tempAns.append(nums[i])
                self.helper(nums, answer, tempAns)
                tempAns.pop(len(tempAns)-1)

    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time.sort()
        count = 0
        for i in range(0, len(time)-1):
            for j in range(i+1, len(time)-1):
                if time[i] <= time[j] and (time[i]+time[j]) % 60 == 0:
                    count += 1
        return count


ss = Solution()
time = [60, 60, 60]
print(ss.numPairsDivisibleBy60(time))
