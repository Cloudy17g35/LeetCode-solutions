class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            if n % 2 == 0:
                d[n] = d.get(n, 0) + 1
        if d:
            return sorted(d.items(), key= lambda x: (x[1], -x[0]))[-1][0]
        return -1
