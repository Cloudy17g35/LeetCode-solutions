'''Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

'''

from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = Counter(arr)
        try:
            return max({k for k,v in frequency.items() if k == v})
        except ValueError:
            return -1
