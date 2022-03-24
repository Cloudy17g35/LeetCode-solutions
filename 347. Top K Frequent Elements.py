from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        
        SortedCount = sorted(d.items() ,key=lambda x : x[1], reverse=True)[:k]
        
        return [value for  value, count in SortedCount]
