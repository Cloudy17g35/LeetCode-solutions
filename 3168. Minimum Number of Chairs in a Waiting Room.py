class Solution:
    def minimumChairs(self, s: str) -> int:
        res = 0
        chairs_needed = 0


        for c in s.lower():
            if c == 'e':
                chairs_needed += 1
            if c == 'l':
                chairs_needed -= 1

            res = max([res, chairs_needed])

        return res


