'''Given a 0-indexed integer array nums, return the smallest index i of nums such that i mod 10 == nums[i], or -1 if such index does not exist.

x mod y denotes the remainder when x is divided by y.

'''

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if (i == 0) and (nums[i] == 0):
                return i
            else:
                try:
                    if i % 10 == nums[i]:
                        return i
                except ValueError:
                    continue
        return -1
