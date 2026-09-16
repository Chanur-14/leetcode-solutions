# #Leetcode No : 1122 Relative Sort Array
# #Topic : Array
# #**Approach:** Use a frequency dictionary to count `arr1`, follow `arr2` order while adding elements, then add remaining elements in ascending order.

# **Time Complexity:** `O(n + m + k log k + km)` for this implementation, where `n = len(arr1)`, `m = len(arr2)`, and `k` = number of distinct elements.

# **Space Complexity:** `O(n)` for the frequency map and result array.

# **Key Concept:** Frequency Map + Custom Ordering + Sorting Remaining Elements.


from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        freq = {}
        for i in arr1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in arr2:
            ans.extend([i] * freq[i])
        for i in sorted(freq):
            if i not in  arr2:
                ans.extend([i] * freq[i])
        return ans
