# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        queue_clone = deque([cloned])
        
        while queue_clone:
            node = queue_clone.popleft()
            
            if node.val == target.val:
                return node
            
            if node.left:
                queue_clone.append(node.left)
            if node.right:
                queue_clone.append(node.right)
