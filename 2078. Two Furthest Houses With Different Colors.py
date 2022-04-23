class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        i, k = 0, len(colors) - 1
        
        maximal_distance = 0
        for i in range(len(colors)):
            for j in range(len(colors) - 1):
                if colors[i] != colors[j + 1] and j - i > maximal_distance:
                    maximal_distance = j - i
                    
        return maximal_distance + 1
