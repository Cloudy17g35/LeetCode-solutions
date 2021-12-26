import numpy as np
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        try:
            return np.array(original).reshape(m, n)
        except:
            return []
