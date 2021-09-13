class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 0
        current_divisor = n
        while current_divisor > 0:
            if divisors > 3:
                break
            if not n % current_divisor:
                divisors += 1
            current_divisor -= 1
        return divisors == 3
