#Leetcode no : 187 Repeated DNA Sequence
#difficulty : Medium

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        n = len(s)
        k = 10
        seen = set()
        answer = set()
        for i in range(0,n-k+1):
            sub = s[i:i+k]
            if sub not in seen:
                seen.add(sub)
            else:
                answer.add(sub)
        return list(answer)