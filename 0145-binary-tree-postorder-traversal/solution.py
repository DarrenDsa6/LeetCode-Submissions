# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr, prev = root, None
        ans, stack = [], []
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and curr.right!=prev:
                curr = curr.right
            else:
                ans.append(curr.val)
                prev = stack.pop()
                curr = None
        return ans
            
                
