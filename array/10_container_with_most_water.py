from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        lo, hi = 0, len(height) - 1
        max_water = 0
        while lo < hi:
            max_water = max(max_water, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_water

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  
    print(sol.maxArea([1, 1]))                          
    print(sol.maxArea([4, 3, 2, 1, 4]))                
