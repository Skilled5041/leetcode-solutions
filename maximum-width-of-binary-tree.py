from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxWidth = 1
        q = deque()
        q.append((root, 0))
        
        while q:
            qLen = len(q)
            maxWidth = max(maxWidth, q[-1][1] - q[0][1] + 1)
            for i in range(qLen):
                node, pos = q.popleft()

                if node.left:
                    q.append((node.left, pos * 2))
                if node.right:
                    q.append((node.right, pos * 2 + 1))

        return maxWidth
