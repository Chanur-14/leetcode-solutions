#Leetcode 1539. Kth Missing Positive Number
#Topic: Array
#Approach: Binary Search
#Difficulty : Easy
#Time Complexity: O(log n)
#Space Complexity: O(1)

from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            missing = arr[mid] - (mid + 1)
            if missing >= k:
                right = mid
            else:
                left = mid + 1
        ans = k + right
        return ans
        