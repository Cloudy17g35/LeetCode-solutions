class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_nums = set()
        
        for n in nums:
            if n in set_of_nums:
                return True
            set_of_nums.add(n)
        return False
