'''You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U').
Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.'''



from collections import Counter
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s1, s2=  Counter(s[:len(s)//2]), Counter(s[len(s)//2:])

        vowels = 'AEIOUaeiou'

        return sum(value for key, value in s1.items() if key in vowels) \
               == sum(value for key, value in s2.items() if key in vowels)
