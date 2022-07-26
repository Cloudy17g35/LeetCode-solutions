class Solution:
    def repeatedCharacter(self, s: str) -> str:
        
        hashSet = set()
        
        for letter in s:
            if letter in hashSet:
                return letter
            hashSet.add(letter)
            
