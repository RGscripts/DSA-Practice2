from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                return 0
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            if rank[px] == rank[py]:
                rank[px] += 1
            return 1

        return n - sum(union(u, v) for u, v in edges)

if __name__ == "__main__":
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[3,4]]))        
    print(sol.countComponents(5, [[0,1],[1,2],[2,3],[3,4]]))   
    print(sol.countComponents(4, []))                           
