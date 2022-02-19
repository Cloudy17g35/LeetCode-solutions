import numpy as np
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        d = {}
        
        for i in range(len(groupSizes)):
            current_number = groupSizes[i]
            
            if current_number not in d:
                d[current_number] = [i]
            else:
                d[current_number].append(i)

        result = []
        
        for key,value in d.items():
            groups= np.array_split(value,len(value) // key)
            for group in groups:
                result.append(group.tolist())
            
        return result
