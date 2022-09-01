class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        i, k = 0, len(s) - 1
        
        while i <= k:
            if not s[i].isalpha():
                i += 1
                continue
            if not s[k].isalpha():
                k -= 1
                continue
            s[i], s[k] = s[k], s[i]
            i += 1
            k -= 1
        return ''.join(s)
