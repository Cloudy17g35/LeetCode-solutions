'''Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.'''


from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {'l': 0, 'o': 0, 'b': 0, 'a': 0, 'n': 0}
        for letter in text:
            if letter in balloon:
                balloon[letter] += 1

        balloon['o'] //= 2
        balloon['l'] //= 2

        return min(balloon.values())
