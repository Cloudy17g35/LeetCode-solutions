class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        hashMap = {}
        for i,row in enumerate(mat):
            number_of_soliders = row.count(1)
            hashMap[i] = number_of_soliders
        
        res = sorted(hashMap.items(), key=lambda x: (x[1], x[0]))
        return [key for key,value in res][:k]
