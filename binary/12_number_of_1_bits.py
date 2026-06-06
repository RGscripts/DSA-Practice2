class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count

if __name__ == "__main__":
    sol = Solution()
    print(sol.hammingWeight(0b00000000000000000000000000001011))  
    print(sol.hammingWeight(0b00000000000000000000000010000000))  
    print(sol.hammingWeight(0b11111111111111111111111111111101))  
