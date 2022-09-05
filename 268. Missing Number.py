class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = set(nums)
        minimal, maximal = 0, len(nums)
        
        
        for i in range(minimal, maximal + 1):
            if i not in nums:
                return i
