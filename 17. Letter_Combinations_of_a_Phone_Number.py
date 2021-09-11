class Solution(object):
    def letterCombinations(self,  digits):
        map_table = {'2': 'abc', '3': 'def',
                    '4': 'ghi', '5': 'jkl',
                    '6': 'mno', '7': 'pqrs',
                    '8': 'tuv', '9': 'wxyz'}
        if not digits:
            return []
        if int(digits) < 10:
            return list(map_table[digits])
        else:
            from itertools import product
            letters = []
        for element in digits:
            letters.append(map_table[element])
        return [''.join(element) for element in product(*letters)]
