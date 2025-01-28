class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        right_sum, left_sum = 0, sum(nums)
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                break
            right_sum += n
            left_sum -= n
            if abs(right_sum - left_sum) % 2 == 0:
                res += 1
        return res
        
