from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[1])
        arrows = 1
        end = points[0][1]
        for p in points[1:]:
            if p[0] > end:
                arrows += 1
                end = p[1]
        return arrows

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
