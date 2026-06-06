from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return True

        return all(union(u, v) for u, v in edges)

if __name__ == "__main__":
    sol = Solution()
    print(sol.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))  
    print(sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]])) 
    print(sol.validTree(1, []))  
