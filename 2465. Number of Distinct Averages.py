class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        i, k = 0, len(nums) - 1
        averages = set()
        
        while i <= k:
            num1, num2 = nums[i], nums[k]
            average = (num1 + num2) / 2
            averages.add(average)
            i += 1
            k -= 1
        return len(averages)
            
        
