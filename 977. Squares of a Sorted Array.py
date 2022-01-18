'''Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.'''


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num ** 2 for num in nums])
