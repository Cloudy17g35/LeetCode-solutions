class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq._heapify_max(nums)
        last_val = 0
        while k:
            cur_val = heapq._heappop_max(nums)
            last_val = cur_val
            k -= 1
        return last_val
