class Solution(object):
    def possibleStringCount(self, word):
        """
        :type word: str
        :rtype: int
        """
        i = 0
        res = 0
        while i < len(word):
            j = i
            consec = 0
            while j < len(word) and word[j] == word[i]:
                consec += 1
                j += 1
            res += consec - 1
            i = j
        return res + 1
