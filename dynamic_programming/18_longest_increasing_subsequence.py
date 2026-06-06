from typing import List
import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for num in nums:
            pos = bisect.bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        return len(sub)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) 
    print(sol.lengthOfLIS([0, 1, 0, 3, 2, 3]))             
    print(sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))          
