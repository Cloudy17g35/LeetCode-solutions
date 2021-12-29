'''Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.'''


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        all_positives = list(range(1, arr[-1] + k + 1))

        return sorted(set(all_positives) - set(arr))[k - 1]
