class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = [] # will keep (number, current minimum of that number)
        cur_min = nums[0]
        
        for n in nums[1:]:
            while stack and n >= stack[-1][0]:
                stack.pop()
            if stack and n > stack[-1][1]:
                return True
            stack.append((n, cur_min))
            cur_min = min(n, cur_min)
        return False        
