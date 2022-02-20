from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = list(word for word in s1.split())
        s2 = list(word for word in s2.split())
        word_counter = Counter(s1 + s2)
        return [word for word, frequency in word_counter.items() if frequency == 1]
