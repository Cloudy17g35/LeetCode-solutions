class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        return sum([queryTime in range(startTime[i], endTime[i] + 1) for i in range(len(startTime))])
