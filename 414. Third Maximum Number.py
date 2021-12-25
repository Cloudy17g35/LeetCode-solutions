'''Given an integer array nums, return the third distinct maximum number in this array. 
If the third maximum does not exist, return the maximum number.'''

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        else:
            return sorted(set(nums), reverse=True)[2]
