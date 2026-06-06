class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
        return a if b == 0 else a & mask

if __name__ == "__main__":
    sol = Solution()
    print(sol.getSum(1, 2))  
    print(sol.getSum(2, 3))   
    print(sol.getSum(-1, 1)) 
