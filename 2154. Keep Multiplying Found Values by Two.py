class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for i in range(len(nums)):
            current_number = nums[i]
            if current_number == original:
                nums[i], original = original, nums[i] * 2
        return original
