class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        center = set(edges[0])
        
        for i in range(1,len(edges)):
            edge = edges[i]
            center = set(edge) & center
        
        return list(center)[0]
