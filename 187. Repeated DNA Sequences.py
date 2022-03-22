class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashMap = {}
        
        for i in range(len(s)):
            substring = s[i:10+i]
            if substring in hashMap:
                hashMap[substring] += 1
            else:
                hashMap[substring] = 1
        return [key for key, value in hashMap.items() if value > 1]
 
