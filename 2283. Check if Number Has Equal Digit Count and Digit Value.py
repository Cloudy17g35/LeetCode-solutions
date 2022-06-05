class Solution:
    def digitCount(self, num: str) -> bool:
        hashMap = Counter(num)
        for i, n in enumerate(num):
            if int(n) != hashMap[str(i)]:
                return False
            
        return True
            
        
