class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = 0
        for i in range(len(s), -1, -1):
            substring = s[:i]
            if substring and substring.count('L') == substring.count('R'):
                
                r += 1
                
        return r
