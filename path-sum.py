# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.pathSum(root, targetSum, 0, False)
    def pathSum(self, root, targetSum, sum, leaf):
        if root is None:
            return leaf and targetSum == sum
        else:
            return self.pathSum(root.left, targetSum, sum + root.val, not root.left and not root.right) or self.pathSum(root.right, targetSum, sum + root.val, not root.left and not root.right)
