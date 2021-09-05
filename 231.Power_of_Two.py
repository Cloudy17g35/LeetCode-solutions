class Solution:
    def isPowerOfTwo(self,n: int) -> bool:
        if n == 1:
            return True
        else:
            current_number = 2
            power = 1
            while current_number <= n:
                if current_number == n:
                    return True
                current_number = 2 ** power
                power += 1
        return False
