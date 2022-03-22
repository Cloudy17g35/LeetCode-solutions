from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        CounterObject = Counter(s)
        r = sorted([(key, value) for key, value in CounterObject.items()] , key=lambda x: x[1], reverse=True)
        return ''.join([letter * value for letter, value in r])
