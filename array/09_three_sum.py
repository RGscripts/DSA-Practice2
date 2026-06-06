from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == 0:
                    result.append([nums[i], nums[lo], nums[hi]])
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif s < 0:
                    lo += 1
                else:
                    hi -= 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1, 0, 1, 2, -1, -4])) 
    print(sol.threeSum([0, 1, 1]))              
    print(sol.threeSum([0, 0, 0]))             
