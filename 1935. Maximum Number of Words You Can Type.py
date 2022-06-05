class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        res = 0
        broken_set = set(brokenLetters)
        for w in text:
            common_part = set(w) & broken_set
            if not common_part:
                res += 1
        return res
        
 
