class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        for n in str(num):
            if num % int(n) == 0:
                res += 1
        return res
