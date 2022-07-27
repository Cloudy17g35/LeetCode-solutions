class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        
        all_pairs = 0
        all_leftovers = 0
        
        
        for count in d.values():
            pairs  = count // 2
            leftovers = count % 2
            all_pairs += pairs
            all_leftovers += leftovers
        return [all_pairs, all_leftovers]
