#Leetcode Problem: 268. Missing Number
#Topic: Array
#Approach: Mathematical Formula
#Difficulty : Easy
#Time Complexity: O(n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = sum(nums)
        expected_sum = n * (n + 1) // 2
        missing_number = expected_sum - actual_sum
        return missing_number