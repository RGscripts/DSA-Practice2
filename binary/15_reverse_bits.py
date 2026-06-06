class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseBits(0b00000010100101000001111010011100))  
    print(sol.reverseBits(0b11111111111111111111111111111101))  
