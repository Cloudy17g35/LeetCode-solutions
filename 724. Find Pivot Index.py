class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        
        sum_left = 0
        
        for i, n in enumerate(nums):
            sum_right = total - n - sum_left
            if sum_right == sum_left:
                return i
            sum_left += n
        return -1
