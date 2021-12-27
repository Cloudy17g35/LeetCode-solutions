class Solution:
        def replaceDigits(self, s: str):

            not_even = False

            if len(s) % 2 == 0:

                s = list(s)
            else:
                not_even = True
                last_element = list(s[-1])
                s = list(s)[:-1]

            k = 2
            for i in range(0, len(s), 2):
                pair = s[i:k]


                letter, digit = pair[0], pair[1]
                new_letter = chr(ord(letter) + int(digit))
                s[k - 1] = new_letter
                k+= 2

            return ''.join(s + last_element) if not_even else ''.join(s)
