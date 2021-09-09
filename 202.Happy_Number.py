class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()

        while n != 1:
            if n in cycle:
                return False
            cycle.add(n)
            n = sum([int(number) ** 2 for number in str(n)])

        return True
