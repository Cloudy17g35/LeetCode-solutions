class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        c = Counter(nums)
        
        for key, val in c.items():
            if val % 2:
                return False
        return True
