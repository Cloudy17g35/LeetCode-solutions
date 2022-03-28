class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        
        return eval('^'.join([str(start + 2 * i) for i in range(n)]))
