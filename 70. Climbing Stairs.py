class Solution:
    def climbStairs(self, n: int) -> int:
        first, sec = 1, 1

        for _ in range(n - 1):
            tmp = first
            first = first + sec
            sec = tmp
        return first
