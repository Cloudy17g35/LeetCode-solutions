class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        prefix = ''
        
        for i,c in enumerate(word):
            if c == ch:
                prefix += c
                return prefix[::-1] + word[i + 1:]
            else:
                prefix += c
        return word
        
