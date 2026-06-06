from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()

if __name__ == "__main__":
    sol = Solution()
    m1 = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(m1)
    print(m1)

    m2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    sol.rotate(m2)
    print(m2)
