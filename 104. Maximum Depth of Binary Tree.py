# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = collections.deque()
        queue.append(root)
        num_node_levels = 1
        levels = 0
        
        while queue:
            node = queue.popleft()
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
            num_node_levels -= 1
            if not num_node_levels:
                levels += 1
                num_node_levels = len(queue)
                
        return levels
