class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                first, second = nums[j], nums[k]
                three_sum = val + first + second
                
                if three_sum < 0:
                    j += 1
                elif three_sum > 0:
                    k -= 1
                else:
                    res.append([val, first, second])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                         
        return res
