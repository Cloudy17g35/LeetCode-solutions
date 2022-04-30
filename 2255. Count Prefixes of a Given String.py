class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        prefix_dict = {i: l for i, l in enumerate(s)}
        count = 0

        for w in words:
            broken = False
            for i,l in enumerate(w):
                letter_from_prefix = prefix_dict.get(i)
                if letter_from_prefix and letter_from_prefix == l:
                    continue
                else:
                    broken = True
                    break

            if not broken:
                count += 1
        return count
