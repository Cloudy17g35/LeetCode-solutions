class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map_table = {'2': 'abc', '3': 'def',
                    '4': 'ghi', '5': 'jkl', 
                    '6': 'mno', '7': 'pqrs',
                    '8': 'tuv', '9': 'wxyz'}
        result = []
        if not digits:
            return result
        if int(digits) < 10:
            return list(map_table[digits])
        else:
            k = 1
            while k != len(digits):
                i = 0
                for j in range(digits_length):
                    
