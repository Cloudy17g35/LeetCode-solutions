class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d1 = {list1[i]: i for i in range(len(list1))}
        d2 = {list2[i]: i  for i in range(len(list2))}
        
        common = set(d1.keys()) & set(d2.keys())
        
        minimal_value = float('inf')
        result = []
        
        
        for restaurant in common:
            sum_of_indicies = d1[restaurant] + d2[restaurant]
            if sum_of_indicies < minimal_value:
                minimal_value = sum_of_indicies
                
                
        for restaurant in common:
            sum_of_indicies = d1[restaurant] + d2[restaurant]
            if sum_of_indicies == minimal_value:
                result.append(restaurant)
                
        return result
