class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        d = collections.Counter(s)
        res = 0
        while True:
            for letter in target:
                if d[letter] == 0:
                    return res
                else:
                    d[letter] -= 1
            res += 1
    
    
