from collections import Counter
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = {chr(i):0 for i in range(97, 123)}
        
        for l in sentence:
            d[l] += 1
        
        return all(d.values())
