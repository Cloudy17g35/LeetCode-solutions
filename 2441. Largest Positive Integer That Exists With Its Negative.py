class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positive = set()
        negative = set()
        
        for n in nums:
            if n > 0:
                positive.add(n)
            if n < 0:
                negative.add(abs(n))
                
        intersection = positive & negative
        
        return max(intersection) if intersection else -1
                
        
        
