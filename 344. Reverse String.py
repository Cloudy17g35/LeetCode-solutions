class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i, k = 0, len(s) - 1
        
        while i < k:
            s[i], s[k] = s[k], s[i]
            i += 1
            k -= 1
            
