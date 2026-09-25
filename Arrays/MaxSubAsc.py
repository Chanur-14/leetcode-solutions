#LEetcode no :1800 Maximum Ascending Subarray Sum
#Approach : Fast-Slow Pointer
#Difficulty : Easy

from typing import List
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        i = 0
        j = 0
        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]
        while j < n:
            if j == 0:
                curr_sum = nums[j]
            elif nums[j] > nums[j-1]:
                curr_sum += nums[j]
            else:
                curr_sum = nums[j]
            max_sum = max(max_sum,curr_sum)
            j += 1
        return max_sum
 
    