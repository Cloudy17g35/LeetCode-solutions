class Solution:
    def findSpecialInteger(self, arr):

        freq_table = {}

        for element in arr:
            if element not in freq_table:
                freq_table[element] = 1
            else:
                freq_table[element] += 1
        return max(freq_table, key = freq_table.get)
