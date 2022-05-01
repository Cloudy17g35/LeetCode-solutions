class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        for letter in word:
            if not letter.isnumeric():
                word = word.replace(letter,' ')
        return len(set([int(n.strip()) for n in word.split()]))
        
