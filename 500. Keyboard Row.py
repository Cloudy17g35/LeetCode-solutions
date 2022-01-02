'''Given an array of strings words, return the words that can be typed using letters of
the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the character'''
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keybord = {0: "qwertyuiop", 1: "asdfghjkl", 2: "zxcvbnm"}

        result = []

        for word in words:
            for row in keybord:
                if not set(word.lower()) - set(keybord[row]):
                    result.append(word)

        return result
