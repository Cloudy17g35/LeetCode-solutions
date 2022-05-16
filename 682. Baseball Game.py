class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        operations = set(['+', 'D', 'C'])
        for o in ops:
            if o not in operations:
                stack.append(int(o))
            if o == '+':
                stack.append(stack[-1] + stack[-2])
            if o == 'D':
                stack.append(stack[-1] * 2)
            if o == 'C':
                stack.pop()
        return sum(stack)
  
