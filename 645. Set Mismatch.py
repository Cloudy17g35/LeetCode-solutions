class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_number = list(set(range(1, len(nums) + 1)) - set(nums))[0]
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                return [num, missing_number]

