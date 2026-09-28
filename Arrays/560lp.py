#Leetcode no 560 Subaaray Sum Equal to k
#approach : Prefix sum + hasing

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*n
        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        count = 0
        freq = {0:1}
        for i in prefix:
            prev_prefix = i - k
            if prev_prefix in freq:
                count += freq[prev_prefix]
            freq[i] = freq.get(i,0) + 1
        return count        