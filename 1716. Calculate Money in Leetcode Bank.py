class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return sum(list(range(1, n + 1)))
        
        total = 0
        bonus = 0
        
        for _ in range(n // 7):
            for x in range(1, 8):
                total += x + bonus
                
            bonus += 1
             
        for y in range(1, (n % 7) + 1):
            total += y + bonus
            
        return total
            
        
