class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = ''

            for i in range(len(s) - 1):
                d1, d2 = int(s[i]), int(s[i + 1])
                cur = (d1 + d2) % 10
                new_s += str(cur)
            s = new_s
        
        return len(set(s)) == 1
