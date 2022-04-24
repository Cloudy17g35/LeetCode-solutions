# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return []
        sorted_values = deque()
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node:
                bisect.insort(sorted_values,node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        tree = TreeNode(sorted_values.popleft())
        tmp = tree
        for v in sorted_values:
            tmp.right = TreeNode(v)
            tmp = tmp.right
        return tree
