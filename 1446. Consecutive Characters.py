class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        i, k = 0, 1
        maximal_length = 1

        while k < len(s):
            cur_length = 1
            while k < len(s) and s[i] == s[k]:
                cur_length += 1
                k += 1
            else:
                i = k
            maximal_length = max(cur_length, maximal_length)
            k += 1

        return maximal_length
