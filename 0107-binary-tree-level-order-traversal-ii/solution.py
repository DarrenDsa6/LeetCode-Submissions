# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = deque()
        queue = deque([root])
        while queue:
            level = []
            for i in range(len(queue)):
                present = queue.popleft()
                level.append(present.val)
                if present.left:
                    queue.append(present.left)
                if present.right:
                    queue.append(present.right)
            ans.appendleft(level)
        return list(ans)
