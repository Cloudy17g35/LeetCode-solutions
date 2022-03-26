class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, k = 0, len(nums) - 1
        
        while l <= k:
            m = (l + k) // 2
            
            if nums[m] > target:
                k = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        
