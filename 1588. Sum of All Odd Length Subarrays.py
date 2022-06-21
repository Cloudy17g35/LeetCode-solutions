class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) % 2:
            maximal_length_subarray = len(arr)
        else:
            maximal_length_subarray = len(arr) - 1

        i = 1
        total = 0
        while i <= maximal_length_subarray:
            for j in range(0, len(arr)):
                cur_arr = arr[j:j + i]
                if len(cur_arr) == i:
                    total += sum(cur_arr)
            i += 2
        return total
      
