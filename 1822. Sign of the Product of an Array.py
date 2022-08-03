class Solution:
    def arraySign(self, nums: List[int]) -> int:
        number_of_mins = 0
        
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                number_of_mins += 1
        return 1 if number_of_mins % 2 == 0 else -1
        
