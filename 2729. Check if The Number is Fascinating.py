class Solution(object):
    def isFascinating(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(n) + str(n * 2) + str(n * 3)
        nums = Counter([str(n) for n in range(1,10)])
        return Counter(s) == nums
        
