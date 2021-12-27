'''You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).

You have to find a permutation of the string where no letter is followed by another letter and no digit is followed by another digit. That is, no two adjacent characters have the same type.

Return the reformatted string or return an empty string if it is impossible to reformat the string.'''
from itertools import permutations
class Solution:
    def reformat(self, s:str):

        nums = [n for n in s if n.isnumeric()]
        letters = [l for l in s if l.isalpha()]

        if abs(len(nums) - len(letters)) > 1:
            return ''
        else:
            a,b = (nums, letters) if len(nums) <= len(letters) else (letters, nums)

        return ''.join(c for pair in zip_longest(b, a) for c in pair if c)
