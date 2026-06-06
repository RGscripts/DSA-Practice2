from typing import Optional
from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return None
        cloned = {}
        queue = deque([node])
        cloned[node] = Node(node.val)
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned[curr].neighbors.append(cloned[neighbor])
        return cloned[node]

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    sol = Solution()
    cloned = sol.cloneGraph(n1)
    print(f"Cloned node val: {cloned.val}")                          
    print(f"Cloned neighbors: {[n.val for n in cloned.neighbors]}")
    print(f"Original is different object: {cloned is not n1}")       
