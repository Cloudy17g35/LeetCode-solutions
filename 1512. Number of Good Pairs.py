'''Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

'''

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        i, k = 0, 1
        count = 0

        for _ in range(len(nums) - 1):
            while k != len(nums):
                if (nums[i] == nums[k]) and (i < k):
                    count += 1
                    k += 1
                else:
                    k += 1

            k = 0

            i += 1


        return count
