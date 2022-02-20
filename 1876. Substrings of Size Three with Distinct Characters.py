class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            part = s[i:3 + i]
            
            if len(part)  == 3 and len(set(part)) == 3:
                count += 1
                
        return count
