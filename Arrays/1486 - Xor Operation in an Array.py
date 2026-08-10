#Leetcode 1486 - Xor Operation in an Array
#Difficulty: Easy
#Time Complexity: O(n)
#space Complexity: O(1)
from typing import List
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start + 2 * i
        return ans
        