class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        res = []
        prev = float('-inf')
        for i, h in enumerate(height):
            if (prev != 0) and (prev > threshold):
                res.append(i)
            prev = h
        return res
