class Solution:
    def findGCD(self, nums):
        maximal = max(nums)
        minimal = min(nums)
        gdc = 1
        if maximal == minimal:
            return maximal

        for x in range(1, maximal + 1):
            if maximal % x == 0 and minimal % x == 0:
                gdc = x
        return gdc
