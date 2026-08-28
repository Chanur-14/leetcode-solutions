#Leetcode 771. Jewels and Stones
#Difficulty: Easy
#Time Complexity: O(n)  
#Space Complexity: O(n)
#Topic: Arrays
from typing import List
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for ch in stones:
            if ch in jewel_set:
                count+=1
        return count