class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if is_palindrome(word):
                return word
        return ''


def is_palindrome(s:str) -> bool:
    i, k = 0, len(s) - 1

    while i <= k:
        if s[i] != s[k]:
            return False
        i += 1; k -= 1
    return True        
