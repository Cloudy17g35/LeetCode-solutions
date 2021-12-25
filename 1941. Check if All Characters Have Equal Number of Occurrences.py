from collections import Counter
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = Counter(s)
        
        return True if len(set(d.values())) == 1 else False
