class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = defaultdict(int)

        index = 0

        for n in nums:
            d[n] += 1
            o = d[n]
            if o <= 2:
                nums[index] = n
                index += 1
        return index
        
