# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.currMax = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.currMax = root.val
        def maxPath(root):
            if not root:
                return 0

            maxLeft = max(maxPath(root.left), 0)
            maxRight = max(maxPath(root.right), 0)

            self.currMax = max(self.currMax, root.val + maxLeft + maxRight)

            return root.val + max(maxLeft, maxRight)

        maxPath(root)
        return self.currMax
