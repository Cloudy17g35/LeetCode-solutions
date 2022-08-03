from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return True if not Counter(ransomNote)  - Counter(magazine) else False
