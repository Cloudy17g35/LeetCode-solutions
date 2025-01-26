class Solution(object):
    def getEncryptedString(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''

        
        for i, c in enumerate(s):
            cur_i = i + k
            if cur_i >= len(s):
                l = s[cur_i % len(s)]
            else:
                l = s[cur_i]
            res += l
        return res
