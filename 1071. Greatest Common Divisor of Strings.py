class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while n % 2:
            n *= 2
        return n
