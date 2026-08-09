#Leetcode 414 - Third Maximum Number
#Difficulty: Easy
#Time Complexity: O(n)
#space Complexity: O(1)
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first =second =third = float('-inf')
        for num in nums:
            if num == first or num == second or num == third:
                continue
            elif num > first:
                third = second
                second = first
                first = num
            elif num > second :
                third = second
                second = num
            elif num > third:
                third = num
        if third == float('-inf'):
            return first
        else:
            return third
        return num