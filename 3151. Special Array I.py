class Solution(object):
    def isArraySpecial(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        i, k = 0, 1

        while i < len(nums) - 1:
            if (nums[i] % 2) and (nums[k] % 2):
                return False
            if (nums[i] % 2 == 0) and (nums[k] % 2 == 0):
                return False
            i += 1; k += 1
        return True
