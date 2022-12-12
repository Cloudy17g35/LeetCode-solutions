class Solution:
    def averageValue(self, nums: List[int]) -> int:
        filtered = [n for n in nums if n % 2 == 0 and n % 3 == 0]
        return sum(filtered) // len(filtered) if filtered else 0
