'''A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.'''
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr)

        r = arr[0] - arr[1]

        if r != 0:
            return list(range(max(arr),min(arr) + r, r))[::-1] == arr
        
        return True if len(set(arr)) == 1 else False
