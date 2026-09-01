#Leetcode Problem 48. Rotate Image
#Topic: Array   
#Difficulty : Medium
#Time Complexity: O(n^2)
#Space Complexity:O(1)

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i].reverse()