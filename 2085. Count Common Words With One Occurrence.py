'''Given two string arrays words1 and words2, return the number of strings that appear exactly once in each of the two arrays.'''

from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        d1 = Counter(words1)
        d2 = Counter(words2)

        return len({key for key,value in d1.items() if value == 1} & {key for key,value in d2.items() if value == 1})
