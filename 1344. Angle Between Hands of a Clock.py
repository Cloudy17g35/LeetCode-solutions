class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        r = abs(1/2 * (60 * hour - 11 * minutes))
        return 360 - r if r > 180 else r
        
