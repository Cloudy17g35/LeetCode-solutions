'''Given the array of integers nums, you will choose two different indices i and j of that array. Return'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        i, j = nums[0], nums[1]
        return (i - 1) * (j - 1)
