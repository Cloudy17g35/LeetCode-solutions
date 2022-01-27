class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiuoAEIUO'

        d1 = {}
        d2 = {}

        for i in range(len(s)):
            char = s[i]

            if char in vowels:
                d1[i] = char

            else:
                d2[i] = char


        d1 = {key:value for key, value in zip(d1.keys(), list(d1.values())[::-1])}

        result =  sorted({**d1, **d2}.items())

        return ''.join([letter for index, letter in result])
