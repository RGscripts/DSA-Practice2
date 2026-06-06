from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo]

if __name__ == "__main__":
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))      
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(sol.findMin([11, 13, 15, 17]))      
