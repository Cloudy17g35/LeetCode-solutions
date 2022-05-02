# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            
            if node and node.val % 2 == 0:
                if node.left and node.left.left:
                    res.append(node.left.left.val)
                if node.left and node.left.right:
                    res.append(node.left.right.val)
                if node.right and node.right.right:
                    res.append(node.right.right.val)
                if node.right and node.right.left:
                    res.append(node.right.left.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return sum(res)
