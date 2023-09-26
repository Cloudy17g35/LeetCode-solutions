class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        words_len, s_len = len(words), len(s)
        
        if words_len != s_len:
            return False
        
        for i in range(words_len):
            if words[i][0] != s[i]:
                return False
        return True
