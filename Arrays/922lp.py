#Leetcode Problem : 922 Sort Array By Parity II
#Topic : Arrays


from typing import List
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        last = len(nums) - 1

        while(even <=last and odd <=last):
            element = nums[last]
            if(element % 2 == 0):
                # If element is even put it in even index
                nums[even],nums[last] = nums[last], nums[even]
                even+=2
            else:
                nums[odd],nums[last] = nums[last], nums[odd]
                odd+=2
        
        return nums
        