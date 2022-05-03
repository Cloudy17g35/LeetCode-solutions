class Solution:
    def freqAlphabets(self, s: str) -> str:
        number_to_letter = {str(i - 96): chr(i) for i in range(97, 123)}
        res = ''
        for i in range(len(s)):
            if s[i:i+3][-1] == '#':
                cur_letter = number_to_letter.get(s[i:i+2])
                if cur_letter:
                    res += cur_letter
            if not '#' in s[i:i +3]:
                res += number_to_letter[s[i]]
                
        return res
