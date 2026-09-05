#Leetcode 643. Maximum Average Subarray I
#Topic: Array
#Approach: Sliding Window
#Difficulty : Easy
#Time Complexity: O(n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        i = 0
        j = 0
        cur_sum = 0
        max_sum = float('-inf')
        while j < n:
            cur_sum += nums[j]
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                max_sum = max(max_sum,cur_sum) 
                cur_sum -= nums[i]
                i += 1
                j += 1
        return max_sum / k      