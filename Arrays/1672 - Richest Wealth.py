#Leetcode 1672 - Richest Customer Wealth
#Difficulty: Easy
#Time Complexity: O(n)
#space Complexity: O(1)
from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        for account in accounts:
            res.append(sum(account))
        return max(res)
