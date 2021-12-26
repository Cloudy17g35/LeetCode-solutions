'''Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.

Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.

The frequency of a letter x is the number of times it occurs in the string.'''

from collections import Counter
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str):

        d1 = Counter(word1)
        d2 = Counter(word2)

        all_keys = set(d1.keys()).union(set(d2.keys()))

        for key in all_keys:
            first = d1.get(key,0)
            second = d2.get(key,0)

            difference = abs(first - second)

            if difference >= 4:
                return False

        return True
