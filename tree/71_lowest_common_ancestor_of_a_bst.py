class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(6)
    p = TreeNode(2)
    q = TreeNode(8)
    root.left = p
    root.right = q
    ans = sol.lowestCommonAncestor(root, p, q)
    print(ans.val)
