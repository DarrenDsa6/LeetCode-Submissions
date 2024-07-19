# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursion(node, target):
            if not node:
                return False
            target -= node.val
            if not node.left and not node.right:
                return target == 0
            return recursion(node.left, target) or recursion(node.right, target)
        return recursion(root, targetSum)
