class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum:int = 0
        digit_sum:int = 0
        for num in nums:
            element_sum += num
            num = str(num)
            for n in num:
                digit_sum += int(n)
        return abs(element_sum - digit_sum)
