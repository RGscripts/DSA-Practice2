from typing import List
from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        in_degree = {c: 0 for word in words for c in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        in_degree[w2[j]] += 1
                    break

        queue = deque(c for c in in_degree if in_degree[c] == 0)
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in adj[c]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return "".join(result) if len(result) == len(in_degree) else ""

if __name__ == "__main__":
    sol = Solution()
    print(sol.alienOrder(["wrt", "wrf", "er", "ett", "rftt"])) 
    print(sol.alienOrder(["z", "x"]))                            
    print(sol.alienOrder(["z", "x", "z"]))                      
