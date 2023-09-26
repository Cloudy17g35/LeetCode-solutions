class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for letter in s:
            if letter == 'i':
                res = res[::-1]
                continue
            res += letter
        return res
