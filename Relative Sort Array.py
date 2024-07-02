class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        c = Counter(arr1)
        result = list()

        for n in arr2:
            occurences = c[n]
            for _ in range(occurences):
                result.append(n)
            del c[n]
        resting_items = sorted(c.items(), key=lambda x: x[0])
        rest = list()
        for item in resting_items:
            num, count = item[0], item[1]
            for _ in range(count):
                rest.append(num)
        return result + rest
