class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        i, k = 0, 1
        unique_sums = set()
        while k < len(nums):
            num1, num2 = nums[i], nums[k]
            cur_sum = sum([num1, num2])
            if cur_sum in unique_sums:
                return True
            unique_sums.add(cur_sum)
            i += 1; k+=1
        return False
