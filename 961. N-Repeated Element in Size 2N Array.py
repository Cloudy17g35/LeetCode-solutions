'''https://leetcode.com/problems/n-repeated-element-in-size-2n-array/'''

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = Counter(nums)


        return [key for key, value in d.items() if value == len(nums) // 2][-1]
