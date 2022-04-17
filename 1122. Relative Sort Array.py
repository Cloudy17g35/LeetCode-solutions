class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        relative_sort_dict = {arr2[i]:i for i in range(len(arr2))}
        result_dict = {}
        others = []
        for num in arr1:
            if num in relative_sort_dict:
                rank = relative_sort_dict[num]
                if rank in result_dict:
                    result_dict[rank].append(num)
                else:
                    result_dict[rank] = [num]
                    
            else:
                others.append(num)
          
        
        result_list = []
        
        for key,value in sorted(result_dict.items()):
            result_list.extend(value)
        
        return result_list + sorted(others)
        
