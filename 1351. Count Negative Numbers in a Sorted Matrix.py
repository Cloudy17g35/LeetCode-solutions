'''Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.'''

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0
        for l in grid:
            row = l
            
            for number in row:
                if number < 0:
                    
                    count += 1
                
        return count  
