class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            d[num] = abs(num - 0)
        min_value = min(d.values())
        return max([key for key,value in d.items() if value == min_value])
