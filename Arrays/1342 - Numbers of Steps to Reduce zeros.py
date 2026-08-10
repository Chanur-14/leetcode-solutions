#Leetcode 1342 - Number of Steps to Reduce a Number to Zero
#Difficulty: Easy
#Time Complexity: O(n)
#space Complexity: O(1)
from typing import List
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num > 0:
            if num % 2 == 0:
                num //= 2
                count += 1
            if num % 2 == 1:
                num -= 1
                count += 1
        return count

        