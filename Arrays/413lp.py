#Leetcode no : 413 Arithmetic Slices
#Difficulty : Medium

from typing import List
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        ans = 0
        for i in range(1,len(nums)-1):
            prev_dif = nums[i] - nums[i-1]
            diff = nums[i+1] - nums[i]
            if diff == prev_dif:
                count += 1
            else:
                count = 0
            prev_dif = diff
            ans += count
        return ans

        