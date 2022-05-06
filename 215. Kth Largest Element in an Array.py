class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # this solution works correctly only for values >= 0
        nums = [-n for n in nums]
        heapq.heapify(nums)
        last_val = 0
        while k:
            cur_val = heapq.heappop(nums)
            last_val = cur_val
            k -= 1
        return abs(last_val)
        
      
