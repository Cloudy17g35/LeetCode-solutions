class Solution:
    def removeDuplicates(self, s: str) -> str:
        i = 0

        while i < len(s) - 1:
            if i >= 0 and s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                i -= 1

            else:
                i += 1

        return s
