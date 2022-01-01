class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        result = []

        for i in range(left, right + 1):
            if not '0' in str(i):
                numbers = [i % int(n) for n in str(i)]

                if not any(numbers):
                    result.append(i)

        return result
