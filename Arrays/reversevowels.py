#Leetcode Problem: 345. Reverse Vowels of a String
#Difficulty: Easy   
#Time Complexity: O(n)  
#Space Complexity: O(n)
#Topic: Arrays
from typing import List
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i = 0
        j = len(s) - 1
        vowels = "AEIOUaeiou"
        while i< j:
            if s[i] not in vowels:
                i += 1
            elif s[j] not in vowels:
                j -=1
            else:
                s[i],s[j] = s[j],s[i]
                i+=1
                j-=1
        return ''.join(s)

        