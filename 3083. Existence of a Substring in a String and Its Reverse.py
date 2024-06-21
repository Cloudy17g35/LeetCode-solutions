class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        i, k = 0, 1
        reversed_s = s[::-1]
        visited = set()
        visited_res = set()

        while i < len(s) - 1:
            sub_1, sub_2 = s[i] + s[k], reversed_s[i] + reversed_s[k]
            if visited & visited_res:
                return True
            else:
                visited.add(sub_1)
                visited_res.add(sub_2)
            i+=1; k+=1
        return True if visited & visited_res else False
