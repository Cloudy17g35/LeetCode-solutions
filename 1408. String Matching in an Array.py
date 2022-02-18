class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        result = set()
        
        for word in words:
            for word_inside in words:
                if (word_inside in word) and (word_inside != word):
                    result.add(word_inside)
                    
        return list(result)
