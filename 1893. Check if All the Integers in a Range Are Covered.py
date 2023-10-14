class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        result = set()
        for r in ranges:
            low_range, high_range = r[0], r[1] 
            for num in range(low_range, high_range + 1):
                if left <= num <= right:
                    result.add(num)

        return result == set(range(left, right + 1)) if result else False a
