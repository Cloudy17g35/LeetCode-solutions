class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        interval = list(range(lo, hi + 1))
        
        hashMap = {}
        
        for n in interval:
            
            x = n
            
            count = 0
            while x != 1:
                if x % 2 == 0:
                    x = x / 2
                else:
                    x = 3 * x + 1
                count += 1
            hashMap[n] = count
        
        return sorted(hashMap.items(), key = lambda x: x[1])[k - 1][0]            
