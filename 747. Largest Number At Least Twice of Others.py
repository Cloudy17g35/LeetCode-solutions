class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximal_value = max(nums)
        maximal_value_index = nums.index(maximal_value)
        limit = maximal_value // 2
        
        for n in nums:
            if (n > limit) and (n != maximal_value):
                return -1
            
        return maximal_value_index
        
