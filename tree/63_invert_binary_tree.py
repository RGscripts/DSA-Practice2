from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted = sol.invertTree(root)
    print(inverted.val, inverted.left.val, inverted.right.val)
