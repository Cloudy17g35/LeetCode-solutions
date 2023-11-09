class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        d = dict()
        max_l = -1


        for i,c in enumerate(s):
            if c in d:
               max_l = max(max_l, i - d[c] - 1)
            else:
                d[c] = i
        return max_l
           
