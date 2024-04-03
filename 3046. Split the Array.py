class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        c = dict()
        for n in nums:
            occurences = c.get(n, 1)
            if occurences == 1:
                c[n] = 1
            if occurences > 2:
                return False
            c[n] += 1
        return True
