class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            # step 1
            groups = [s[i:i +k] for i in range(0,len(s), k)]
            # step 2
            sums = []
            for group in groups:
                cur_sum = 0
                for digit in group:
                    cur_sum += int(digit)
                sums.append(str(cur_sum))
                # step 3 - merge
                s = ''.join(sums)
        return s
        
