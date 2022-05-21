class Solution:
    def arrangeCoins(self, n: int) -> int:
        # O(n) solution
        cur_coins = 1
        res = 0
        while n > 0:
            n -= cur_coins
            cur_coins += 1
            if n >= 0:
                res += 1
        return res


s = Solution()
assert s.arrangeCoins(5) == 2
assert s.arrangeCoins(6) == 3
assert s.arrangeCoins(1) ==1