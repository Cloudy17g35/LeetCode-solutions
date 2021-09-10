class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for number in nums:
            rob1, rob2 = rob2, max(rob1 + number, rob2)
        return rob2
