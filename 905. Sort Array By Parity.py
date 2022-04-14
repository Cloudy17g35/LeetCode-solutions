class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            even, odd = [], []
            
            for n in nums:
                if n % 2:
                    odd.append(n)
                else:
                    even.append(n)
            return even + odd
