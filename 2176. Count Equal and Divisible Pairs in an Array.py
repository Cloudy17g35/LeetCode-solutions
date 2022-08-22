class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                num1 = nums[i]
                num2 = nums[j]
                if (num1 == num2) and (i * j) % k == 0:
                    res += 1
        return res
