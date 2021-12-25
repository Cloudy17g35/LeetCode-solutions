# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        begin=1
        end=n
        middle=(begin+end)//2
        while begin <= end:
            
            if guess(middle)==0: return middle
            
            if guess(middle)==-1: 
                end=middle-1
                middle=(begin+end)//2
                
            if guess(middle)==1:
                begin=middle+1
                middle=(begin+end)//2
        
        return middle
