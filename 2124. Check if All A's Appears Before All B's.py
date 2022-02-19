class Solution:
    def checkString(self, s: str) -> bool:
        
        if (not 'a' in s) or (not 'b' in s):
            return True
        
        first_b_occurence = s.index('b')
        
        if set(s[:first_b_occurence]) == set('a') and set(s[first_b_occurence:]) == set('b'):
            return True
        else:
            False
