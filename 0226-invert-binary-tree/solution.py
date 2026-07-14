# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root
        self.invert(head)
        return root

    def invert(self, head: Optional[TreeNode]) -> Optional[TreeNode]:
        if(head and (head.left or head.right)):
            head.left, head.right = head.right, head.left
            self.invert(head.left)
            self.invert(head.right)


    
