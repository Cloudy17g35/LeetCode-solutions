class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, l = 0, len(numbers) - 1

        while i != l:
            sum = numbers[i] + numbers[l]
            if sum > target:
                l -= 1
            elif sum < target:
                i += 1
            else:
                return [i + 1,l + 1]
