class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        set_of_numbers = set(range(1, k + 1))
        for c,num in enumerate(nums[::-1], start=1):
            if num in set_of_numbers:
                k -= 1
                set_of_numbers.discard(num)
            if k == 0:
                return c

