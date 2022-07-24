class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        c1 = collections.Counter(t)
        c2 = collections.Counter(s)
        return True if not (c2 - c1) else False
        
