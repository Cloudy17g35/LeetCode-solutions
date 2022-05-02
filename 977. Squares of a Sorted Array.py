'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        i, k = 0, len(nums) - 1
        
        while i <= k:
            if nums[i] ** 2 > nums[k] **2:
                res.append(nums[i] ** 2)
                i += 1
            else:
                res.append(nums[k] ** 2)
                k -= 1
        return res[::-1]
