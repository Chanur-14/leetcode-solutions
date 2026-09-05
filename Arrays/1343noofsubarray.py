#Leetcode 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
#Topic: Array
#Approach: Sliding Window
#Difficulty : Medium
#Time Complexity: O(n)
#Space Complexity: O(1)
from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        i = 0
        j = 0
        n = len(arr)
        cur_sum = 0
        max_sum = float('-inf')
        count = 0
        while j < n:
            cur_sum += arr[j]
            if (j - i + 1) < k:
                j += 1
            elif (j - i + 1) == k:
                if cur_sum / k >= threshold:
                    count += 1
                cur_sum -= arr[i]
                i += 1
                j += 1
        return count
                