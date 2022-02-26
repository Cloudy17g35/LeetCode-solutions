class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
                
        return len([word for word 
                    in words if not set(word) - set(allowed)])
        
