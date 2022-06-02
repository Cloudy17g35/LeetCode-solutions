class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        
        hash_set = set()
        for i in range(len(s) - k + 1):
            hash_set.add(s[i:i + k])
        return len(hash_set)  == 2 ** k
