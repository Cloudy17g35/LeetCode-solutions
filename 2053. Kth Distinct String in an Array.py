'''A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.'''



from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = OrderedCounter(arr)
        keys_with_one_occurence = {key for key, value in d.items() if
                                  value == 1}

        if len(keys_with_one_occurence) < k:
            return ''

        n = 0
        for key, value in d.items():
            if value == 1:
                n += 1
            if n == k:
                return key
