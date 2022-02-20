class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        arr_length = len(arr)
        cut = int(arr_length * 0.05)
        arr = arr[cut:-cut]
        return sum(arr) / len(arr)
