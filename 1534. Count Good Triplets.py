'''Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x.

Return the number of good triplets.'''

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        all_combinations = list(combinations(arr, 3))

        result = []

        for combination in all_combinations:
            i, j, k = combination

            if (abs(i - j) <= a) and (abs(j - k) <= b) and (abs(i - k) <= c):
                result.append(combination)

        return len(result)

        
        
        
