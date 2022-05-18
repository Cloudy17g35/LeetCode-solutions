class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # if all are True then collision occurs
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    # loop will stop
                    a = 0
                else:
                    a = 0
                    stack.pop()
            # if a is positive or negative we re going to add it
            if a:       
                stack.append(a)
        return stack
