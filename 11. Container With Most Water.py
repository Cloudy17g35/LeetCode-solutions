class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                # minimal height can be taken
                area = (r - l) * min(height[l], height[r])
                result = max(area, result)

        return result
