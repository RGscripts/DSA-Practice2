from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(sol.eraseOverlapIntervals([[1,2],[1,2],[1,2]]))
    print(sol.eraseOverlapIntervals([[1,2],[2,3]]))
