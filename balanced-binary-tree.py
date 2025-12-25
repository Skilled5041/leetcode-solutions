# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
    def depth(self, root):
        if root in self.memo:
            return self.memo[root]

        if root is None:
            return 0
        result = 1 + max(self.depth(root.left), self.depth(root.right))
        self.memo[root] = result
        return result

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
