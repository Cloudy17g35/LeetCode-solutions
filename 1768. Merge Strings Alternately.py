class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        shorter, longer = sorted([word1, word2], key=len)
        merged = ''
        
        last_i = 0
        for i in range(len(shorter)):
            merged += word1[i]
            merged += word2[i]
            last_i = i
        if longer[last_i + 1:]:
            merged += longer[last_i + 1:]
        return merged
