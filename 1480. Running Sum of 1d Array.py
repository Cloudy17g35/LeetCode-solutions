'''Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

'''


from itertools import accumulate


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
