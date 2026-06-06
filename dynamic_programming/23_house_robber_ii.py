from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(arr):
            prev2, prev1 = 0, 0
            for num in arr:
                prev2, prev1 = prev1, max(prev1, prev2 + num)
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([2, 3, 2]))        
    print(sol.rob([1, 2, 3, 1]))      
    print(sol.rob([1, 2, 3]))         
