class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_lenght = len(nums)
        return sum([nums[i] ** 2 for i in range(len(nums)) if nums_lenght % (i + 1) == 0])
        
