#Leetcode no : 2574 Left and Right Sum Difference
#Approach : Prefix Sum
#Topic : Arrays
from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        left = [0]*n
        right = [0]*n
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        total = prefix[n-1]
        for i in range(n-1):
            left[i+1] = left[i] + nums[i]
            right[i] = total - prefix[i]
        for x in range(n):
            result.append(abs(left[x]-right[x]))

        return result
            