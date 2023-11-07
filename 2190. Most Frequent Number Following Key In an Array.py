from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        i, k = 0, 1

        d = defaultdict(int)
        while i < len(nums) and k < len(nums):
            if nums[i] == key:
                target = nums[k]
                d[target] += 1
            i += 1; k+=1
        
        return sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]
        
