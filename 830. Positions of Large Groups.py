class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        res = []
        if len(s) < 3:
            return res
        i, k = 0, 1
        while i != len(s):
            group = []
            while k <= len(s) - 1 and s[i] == s[k]:
                group.append(i)
                i += 1
                k += 1
            if len(group) >= 2:
                res.append([min(group), max(group) + 1])
            i += 1
            k += 1
        return res
