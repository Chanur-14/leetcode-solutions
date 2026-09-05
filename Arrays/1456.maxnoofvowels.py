#Leetcode 1456. Maximum Number of Vowels in a Substring of Given Length
#Topic: String
#Approach: Sliding Window
#Difficulty: Medium
#Time Complexity: O(n)
#Space Complexity: O(1)

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i = 0
        j = 0
        curr_count = 0
        max_count = float('-inf')
        while j < len(s):
            vowels = "aeiou"
            if s[j] in vowels:
                curr_count += 1
            if (j - i + 1) < k:
                j += 1
            elif (j - i + 1) == k:
                max_count = max(max_count,curr_count)
                if s[i] in vowels:
                    curr_count -= 1
                i += 1
                j += 1
        return max_count