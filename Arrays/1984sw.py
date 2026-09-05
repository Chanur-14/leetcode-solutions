#Leetcode 1984. Minimum Difference Between Highest and Lowest of K Scores
#Topic: Array       
#Approach: Sliding Window
#Difficulty : Easy
#Time Complexity: O(nlogn)
#Space Complexity: O(1)
from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        min_diff = float('inf')
        nums.sort()
        while j < len(nums):
            if (j - i + 1) < k :
                j += 1
            elif (j - i + 1) == k:
                diff = nums[j] - nums[i]
                min_diff = min(min_diff,diff)
                i += 1
                j += 1
        return min_diff

        