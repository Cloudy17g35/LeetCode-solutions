class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        cs, ct = dict(), dict()
        for i, (s1, s2) in enumerate(zip(s,t)):
            cs[s1] = i; ct[s2] = i
        
        res = 0

        for l in cs:
            index_c = cs[l]
            index_t = ct[l]
            res += abs(index_c - index_t)
        return res
