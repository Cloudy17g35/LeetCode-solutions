class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        i = 0
        while i < len(s) - 1:
            if s == goal:
                return True
            s = s[1:] + s[0]
            i += 1
        return s == goal

  
