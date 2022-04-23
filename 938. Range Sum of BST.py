# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        res = 0
        queue = deque()
        queue.append(root)
        range_of_values = range(low, high + 1)
        
        while queue:
            node = queue.popleft()
            if node and node.val in range_of_values:
                res += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return res
        
