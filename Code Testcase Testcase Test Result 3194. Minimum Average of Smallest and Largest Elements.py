class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        res = float('inf')
        i, k = 0, len(nums) - 1

        while i <= k:
            res = min([res, (nums[i] + nums[k]) / 2])
            i += 1; k-=1
        return res

    
