class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return next(iter(set(range(0, len(nums) + 1)) - set(nums)))
