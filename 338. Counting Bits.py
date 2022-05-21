from typing import List
class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        for i in range(n + 1):
            num_bits = 0
            while i:
                num_bits += i & 1
                i >>= 1
            res.append(num_bits)
        return res

