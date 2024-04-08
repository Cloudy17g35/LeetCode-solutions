class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        c = Counter(students)
        res = len(students)
        
        for s in sandwiches:
            if c[s] > 0:
                res -= 1
                c[s] -= 1
            else:
                return res

        return res
