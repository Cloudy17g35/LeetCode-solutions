class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr)

        r = arr[0] - arr[1]

        if r != 0:
            return list(range(max(arr),min(arr) + r, r))[::-1] == arr
        
        return True if len(set(arr)) == 1 else False
