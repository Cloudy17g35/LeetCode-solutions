class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        d = {chr(i): i - 97 for i in range(97,107)}
        
        first_sum = int(''.join([str(d[letter]) for letter in firstWord]))
        second_sum = int(''.join([str(d[letter]) for letter in secondWord]))
        target_sum = int(''.join([str(d[letter]) for letter in targetWord]))
        
        return first_sum + second_sum == target_sum
        
