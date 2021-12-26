class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        numbers = [int(i) for i in s.split() if i.isnumeric()]
        i, k = 0, 1

        while k != len(numbers) :
            if numbers[k] <= numbers[i]:
                return False
            i += 1
            k += 1

        return True
