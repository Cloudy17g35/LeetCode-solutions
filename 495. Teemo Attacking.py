class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = duration
        

        for i in range(0,len(timeSeries)-1):
            res += min(timeSeries[i+1] - timeSeries[i], duration)

        return res
