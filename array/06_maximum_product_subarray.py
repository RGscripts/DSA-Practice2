from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        for num in nums[1:]:
            candidates = (num, max_prod * num, min_prod * num)
            max_prod = max(candidates)
            min_prod = min(candidates)
            result = max(result, max_prod)
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2, 3, -2, 4]))   
    print(sol.maxProduct([-2, 0, -1]))    
    print(sol.maxProduct([-2, 3, -4]))    
