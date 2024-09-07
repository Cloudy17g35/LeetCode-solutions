class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        d = defaultdict(set)
        
        for i,n in enumerate(nums):
            d[n].add(i)
            
        while k:
            min_num = min(d)
            indexes = d[min_num]
            closest_index = min(indexes)
            num = nums[closest_index]
            num_multiplied = num * multiplier
            d[min_num].discard(closest_index)
            if not d[min_num]:
                del d[min_num]
            d[num_multiplied].add(closest_index)
            nums[closest_index] = num_multiplied
            k -= 1

        return nums

            
