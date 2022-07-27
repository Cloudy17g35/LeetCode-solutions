class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minimal_diff = float('inf')
        res = []
        for i in range(len(arr) - 1):
            minimal_diff = min(minimal_diff, arr[i + 1] - arr[i])
        
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minimal_diff:
                res.append([arr[i], arr[i + 1]])
        return res
