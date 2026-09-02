#Leetcode Problem: 1385. Find the Distance Value Between Two Arrays
#Topic: Array
#Approach: Brute Force
#Difficulty : Easy
#Time Complexity: O(n*m)
#Space Complexity: O(1)

from typing import List
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for i in range(len(arr1)):
            is_valid = True
            for j in range(len(arr2)):
                if abs(arr1[i] - arr2[j]) <= d:
                    is_valid = False
                    break
            if is_valid:
                ans += 1
        return ans
        