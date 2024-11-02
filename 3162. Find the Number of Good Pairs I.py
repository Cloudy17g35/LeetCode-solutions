class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for n1 in nums1:
            for n2 in nums2:
                if n1 % (n2 * k) == 0:
                    res += 1
        return res
        
