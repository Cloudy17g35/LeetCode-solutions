class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maximal_sequence = 0
        
        for n in nums:
            if (n - 1) not in nums:
                cur_length = 0
                while (n + cur_length) in nums:
                    cur_length += 1
                maximal_sequence = max(maximal_sequence, cur_length)
        return maximal_sequence
