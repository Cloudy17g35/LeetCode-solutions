# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        
        d = set()
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            
            if node:
                cur_val = node.val
                diff = k - cur_val
                if diff in d:
                    return True
                else:
                    d.add(cur_val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
