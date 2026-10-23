#Leetcode no : 2460 Apply array operations
#Topic : Array
#Appraoch : Two Pointers and Move Zeros
#Difficulty : Easy

from typing import List
class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        i = 0
        j = i+1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
            elif nums[i] != nums[i+1]:
                i += 1
            else:
                continue
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[k] = nums[k],nums[i]
                k+=1
        return nums
        