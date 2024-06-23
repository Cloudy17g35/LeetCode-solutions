class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        res = []
        for i in range(len(mountain) - 2):
            n1, n2, n3 = mountain[i], mountain[i + 1], mountain[i + 2]

            if n1 < n2 > n3:
                res.append(i + 1)

        return res

