class Solution:
    def findContentChildren(self, g: List[int], s: List[int]):
        g.sort()
        s.sort()
        total = 0
        for i in range(0, len(s)):
            if g and s[i] >= g[0]: # if child is satisfied with current cookie
                total += 1
                g.pop(0)
        return total
