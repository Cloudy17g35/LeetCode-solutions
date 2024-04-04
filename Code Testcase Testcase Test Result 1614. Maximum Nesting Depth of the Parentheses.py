class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        stack = []
        for l in s:
            if l == '(':
                stack.append(l)
                depth = max(depth, len(stack))
            if l == ')':
                stack.pop()
        return depth
        
