#Leetcode no : 16 3 sum closest
#Difficulty : Medium
#Topic : Arrays
#Appraoch : Two Pointers

from List import typing
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        i = 0
        closest = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total-target) < abs(closest-target):
                    closest = total
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total
        return closest
