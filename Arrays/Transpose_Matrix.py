#Leetcode 867 - Transpose Matrix
#Difficulty: Easy
#Time Complexity: Time: O(n²)
#space Complexity: Space: O(n²) 
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        result = [[0]*r for _ in range(c)]
        for i in range(r):
            for j in range(c):
                result[j][i] = matrix[i][j]
        return result
        