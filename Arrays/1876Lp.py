#Leetcode 1876. Substrings of Size Three with Distinct Characters
#Topic: String
#Approach: Sliding Window
#Difficulty: Easy
#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        i = 0
        j = 0
        count = 0
        while j < len(s):
            if (j - i + 1) < 3:
                j += 1
            elif (j - i + 1) == 3:
                window = s[i],s[i+1],s[j]
                if len(set(window)) == 3:
                    count += 1
                i += 1
                j += 1
        return count