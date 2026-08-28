#Topic: Arrays
#Leetcode Problem: 645. Set Mismatch
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(n)
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        ans = []
        for key,value in count.items():
            if value == 2:
                ans.append(key)
        for i in range(1,len(nums)+1):
            if i not in nums:
                ans.append(i)
        return ans