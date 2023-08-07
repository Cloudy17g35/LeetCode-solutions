class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        maximal_res = float('-inf')
        for i,n in enumerate(number):
            if n == digit:
                candidate = number[:i] + number[i + 1:]
                maximal_res = max([maximal_res, candidate])
        return maximal_res
