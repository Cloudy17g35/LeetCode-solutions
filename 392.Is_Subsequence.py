class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        map_table = {}
        i = 0
        for letter in t:
            if letter in s:
                map_table[letter] = i
            i += 1

        return ''.join(element[0] for element in sorted(map_table.items(), key=lambda x: x[1])) == s
