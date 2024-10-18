class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_sum = float('inf')
        for n in nums:
            cur_sum = sum([int(i) for i in str(n)])
            min_sum = min(min_sum, cur_sum)
        return min_sum
