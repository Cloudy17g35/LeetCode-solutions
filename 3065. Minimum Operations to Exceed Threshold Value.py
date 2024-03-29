import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        c = 0
        while True:
            if heapq.heappop(nums) >= k:
                break
            c += 1
        return c
