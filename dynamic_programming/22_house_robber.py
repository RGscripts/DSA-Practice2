from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        for num in nums:
            prev2, prev1 = prev1, max(prev1, prev2 + num)
        return prev1

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1, 2, 3, 1]))      
    print(sol.rob([2, 7, 9, 3, 1]))   
