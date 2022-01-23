from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = Counter(s)
        d2 = Counter(t)
        return ''.join((d2 - d1).keys())
