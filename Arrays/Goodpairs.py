#Topic: Arrays
#Leetcode Problem: 1512. Number of Good Pairs
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(n)

from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        ans = 0
        for x in nums:
            if x in count:
                ans += count[x]
                count[x] += 1
            else:
                count[x] = 1
        return ans
        