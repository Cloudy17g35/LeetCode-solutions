class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s = {}, {}
        
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            # there is different mapping
            if ((char_s in s_to_t and s_to_t[char_s] != char_t) or
            (char_t in t_to_s and t_to_s[char_t] != char_s)):
                return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        return True
