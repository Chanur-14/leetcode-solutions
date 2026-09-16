#Leetcode no : 80 Remove Element From Sorted Array II
#Topic : Array
#Level : Medium
#Appraoch : Two - Pointers

from typing import List
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 2
        for i in range(2,len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
        