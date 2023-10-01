class Solution(object):
    def numberOfPoints(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        result = set()

        for n in nums:
            for i in range(n[0], n[1] + 1):
                result.add(i)
        return len(result)
