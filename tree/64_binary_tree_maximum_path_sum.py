from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [float('-inf')]
        def dfs(node):
            if not node:
                return 0
            leftMax = max(dfs(node.left), 0)
            rightMax = max(dfs(node.right), 0)
            res[0] = max(res[0], node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        dfs(root)
        return res[0]

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    print(sol.maxPathSum(root))
