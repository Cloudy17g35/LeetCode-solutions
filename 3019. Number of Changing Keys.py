class Solution:
    def countKeyChanges(self, s: str) -> int:
        i,k = 0, 1
        c = 0
        while k <= len(s) - 1:
            if s[i].lower() == s[k].lower():
                i+=1;k+=1
                continue
            else:
                c += 1
            i+=1;k+=1

        return c
