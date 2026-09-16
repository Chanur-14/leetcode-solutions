#Leetcode no : 56 Merge Intervals

from typing import List
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        ans = []
        ans.append(intervals[0])
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],end)
            else:
                ans.append(interval)
        return ans

        