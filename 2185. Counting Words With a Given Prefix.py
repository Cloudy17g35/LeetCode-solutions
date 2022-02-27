class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for word in words:
            for i in range(len(pref)):
                
                if pref[:i + 1] != word[:i + 1]:
                    break
                
                if (pref[:i +1] == pref) and pref[:i + 1] == word[:i+1]:
                    count += 1
                    
        return count  
