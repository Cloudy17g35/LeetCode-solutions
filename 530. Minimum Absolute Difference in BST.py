# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        sorted_values = []
        
        while queue:
            node = queue.popleft()
            if node:
                bisect.insort(sorted_values, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        min_diff = float('inf')
        
        for i in range(len(sorted_values) - 1):
            if abs(sorted_values[i] - sorted_values[i + 1]) < min_diff:
                min_diff = abs(sorted_values[i] - sorted_values[i + 1])
        return min_diff
        
