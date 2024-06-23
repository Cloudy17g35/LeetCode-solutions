class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        divisible_by_three = set([n for n in range(0, 51) if not n % 3])
        o = 0

        for n in nums:
            if n in divisible_by_three:
                continue
            n_add = n
            n_substract = n
            while True:
                if n_add in divisible_by_three:
                    o += 1
                    break
                if n_substract in divisible_by_three:
                    o += 1
                    break
                n_add += 1
                n_substract -= 1
                
        return o
