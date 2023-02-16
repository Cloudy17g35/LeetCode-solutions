class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        res = float('-inf')
        for s in strs:
            if s.isnumeric():
                value = int(s)
                res = max(value, res)
            else:
                value = len(s)
                res = max(value, res)
        return res
