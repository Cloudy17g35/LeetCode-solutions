class Solution(object):
    def isBalanced(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        odd = 0
        even = 0

        for i, n in enumerate(num):
            if i % 2:
                odd += int(n)
            else:
                even += int(n)
        return odd == even
