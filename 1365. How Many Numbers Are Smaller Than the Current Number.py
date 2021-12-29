'''Given the array nums, for each nums[i] find out how many numbers in the array
are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

'''


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        result = []

        for i in range(len(nums)):
            number = nums[i]
            temp = nums[:i] + nums[i + 1:]

            count = 0

            for n in temp:
                if number > n:
                    count += 1



            result.append(count)

        return result
