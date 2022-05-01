class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        def get_product(n):
            res = 1
            for number in str(n):
                res *= int(number)
            return res if n > 0 else 0
        return get_product(n) - sum([int(number) for number in str(n)])
 
 
