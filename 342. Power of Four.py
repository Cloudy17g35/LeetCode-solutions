class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1 or n == 4:
            return True
        base = 4
        
        while base < n:
            base *= 4
            if base == n:
                return True
        return False
