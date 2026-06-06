from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def bfs(starts):
            visited = set(starts)
            queue = deque(starts)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and heights[nr][nc] >= heights[r][c]:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return visited

        pacific  = bfs([(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)])
        atlantic = bfs([(r, cols-1) for r in range(rows)] + [(rows-1, c) for c in range(cols)])
        return sorted([r, c] for r, c in pacific & atlantic)

if __name__ == "__main__":
    sol = Solution()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print(sol.pacificAtlantic(heights))
    
