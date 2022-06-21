class Solution:
    def greatestLetter(self, s: str) -> str:

        hashSet = set()
        maximal_ord = 0
        maximal_letter = ''
        for letter in s:
            hashSet.add(letter)
            if letter.lower() in hashSet and letter.upper() in hashSet:

                if ord(letter.lower()) > maximal_ord:
                    maximal_ord = ord(letter.lower())
                    maximal_letter = letter.upper()

        return maximal_letter
