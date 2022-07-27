class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        res = ''
        def check_if_good(n:str):
            return len(set(n)) == 1 and len(n) == 3
        
        for i in range(len(num)):
            current_substring = num[i:i + 3]
            if check_if_good(current_substring) and current_substring > res:
                res = current_substring
        return res
