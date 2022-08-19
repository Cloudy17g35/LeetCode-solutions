class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        ret = {}
        
        for val, weight in items1:
            if val not in ret:
                ret[val] = weight
            else:
                ret[val] += weight
        
        for val, weight in items2:
            if val not in ret:
                ret[val] = weight
            else:
                ret[val] += weight
        
        return sorted(ret.items(), key=lambda x: x[0])
