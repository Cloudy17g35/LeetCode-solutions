class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]

        i, k = 0,1
        while k != len(arr):
            arr[i] = max(arr[k:])
            i += 1
            k += 1
        return  arr[:-1] + [-1]
