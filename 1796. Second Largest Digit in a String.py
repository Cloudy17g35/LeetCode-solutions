class Solution:
    def secondHighest(self, s: str) -> int:
        numbers = [n for n in s if n.isnumeric()]
        return sorted(set(numbers),reverse=True)[1] if len(sorted(set(numbers))) > 1 else -1
