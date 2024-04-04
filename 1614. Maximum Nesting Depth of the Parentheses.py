class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        curr = 0
        for l in s:
            if l == '(':
                curr += 1
                depth = max(depth, curr)
            if l == ')':
                curr -= 1
        return depth
        
