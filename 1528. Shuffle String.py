'''You are given a string s and an integer array indices of the same length. 
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.'''

Return the shuffled string.
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        d = {}
        for i in range(len(s)):
            d[indices[i]] = s[i]

        d = sorted(d.items())

        return ''.join(letter for index, letter in d)
