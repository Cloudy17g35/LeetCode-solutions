class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        res = 0
        visited = set()
        for i in range(0, len(words)):
            for j in range(1, len(words)):
                if i == j:
                    continue
                if words[i] == words[j][::-1] and words[i] not in visited and words[j] not in visited:
                    res +=1
                    visited.add(words[i]);visited.add(words[j])
        return res
        
