class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            matrix = sum(matrix, [])
        
            for number in matrix:
                if number == target:
                    return True
                if number > target:
                    return False
