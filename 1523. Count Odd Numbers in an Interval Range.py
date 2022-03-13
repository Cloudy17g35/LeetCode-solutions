class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        odd_lowerbound, odd_uperbound = -1, -1
        
    
        if low % 2:
            odd_lowerbound = low
        else:
            odd_lowerbound = low + 1
            
        if high % 2:
            odd_uperbound = high
        else:
            odd_uperbound = high - 1
            
        
        return (odd_uperbound - odd_lowerbound) // 2 + 1
