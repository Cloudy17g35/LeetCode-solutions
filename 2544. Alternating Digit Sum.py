 class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = 0
        for i, num in enumerate(str(n)):
            if i % 2:
                res -= int(num)
            else:
                res += int(num)
        return res
