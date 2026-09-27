#leetcode no : 3191 Minimum operations to make binary array elements equal to one I
#Approach : Greedy Method + Simulation
#Difficulty : Medium
#Topic : array

from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if i + 2 < len(nums):
                    nums[i] = 1 - nums[i]
                    nums[i+1] = 1 - nums[i+1]
                    nums[i+2] = 1 - nums[i+2]
                    count += 1
                else:
                    return -1
        return count