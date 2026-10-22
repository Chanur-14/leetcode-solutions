#Leetcode no 633 : Sum of Square Numbers
#Topic : Arrays
#difficulty : Medium
#Appraoch : Two Pointers

from typing import List
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        while left <= right:
            total = left * left + right * right
            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1
        return False