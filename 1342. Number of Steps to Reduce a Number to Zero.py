'''Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.'''

class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num /= 2
            result += 1

        return result
