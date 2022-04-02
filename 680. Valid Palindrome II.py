class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, k = 0, len(s) - 1
        
        while i < k:
            if s[i] != s[k]:
                skip_l, skip_r = s[i + 1: k + 1], s[i:k]
                return skip_l == skip_l[::-1] or skip_r == skip_r[::-1]
            i += 1
            k -= 1
                
            
        return True
