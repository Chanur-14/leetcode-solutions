#1446. Consecutive Characters
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def maxPower(self, s: str) -> int:
        current = 1
        max_streak = 1
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                current += 1
            else:
                current = 1
            if current > max_streak:
                max_streak = current
        return max_streak
        