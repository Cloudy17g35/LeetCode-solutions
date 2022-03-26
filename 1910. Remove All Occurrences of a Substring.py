class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            left_i = s.find(part)
            right_i = left_i + len(part)
            s = s[:left_i] + s[right_i:]
        return s
