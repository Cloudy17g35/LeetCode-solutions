class Solution:
    def countAsterisks(self, s: str) -> int:
        line_count: int = 0
        res: int = 0

        for char in s:
            if char == '|':
                line_count += 1
            if char == '*' and line_count % 2 == 0:
                res += 1
        return res
