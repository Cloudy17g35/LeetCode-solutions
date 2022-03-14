class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, k = 0, len(numbers) - 1
        
        while i < k:
            current_sum = numbers[i] + numbers[k]
            
            if current_sum > target:
                k -= 1
            elif current_sum < target:
                i += 1
            else:
                return i + 1, k + 1
