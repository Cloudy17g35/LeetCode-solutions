'''Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.'''


from itertools import combinations
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum(abs(i - j) == k for i, j in combinations(nums, 2))
