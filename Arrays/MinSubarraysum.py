#Leetcode 209. Minimum Size Subarray Sum
#Topic: Array
#Approach: Sliding Window
#Difficulty : Medium
#Time Complexity: O(n)
#Space Complexity: O(1)


from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 0
        curr_sum = 0
        min_sum = float('inf')
        while j < n:
            curr_sum += nums[j]
            while curr_sum >= target:
                min_sum = min(min_sum,j-i+1)
                curr_sum -= nums[i]
                i += 1
            j += 1
        return 0 if min_sum == float('inf') else min_sum
        