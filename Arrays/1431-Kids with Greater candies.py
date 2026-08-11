#Leetcode Problem 1431: Kids With the Greatest Number of Candies
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for candy in candies:
            if candy + extraCandies >= max(candies):
                res.append(True)
            else:
                res.append(False)
        return res