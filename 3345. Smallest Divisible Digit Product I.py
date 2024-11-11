class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product = 1
            for num in str(n):
                num = int(num)
                product *= num
            
            if product % t:
                n += 1
            else:
                return n
