class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = {height:name for height,name in zip(heights, names)}
        return [name for _, name in sorted(d.items(), key = lambda x: x[0], reverse=True)]
        
