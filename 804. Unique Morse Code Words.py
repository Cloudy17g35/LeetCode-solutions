class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code_letters = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-"
                              ,".-..","--","-.","---",".--.","--.-",".-."
                              ,"...","-","..-","...-",".--","-..-","-.--","--.."]
        
        morse_to_alpha = {chr(i): letter for i, letter in enumerate(morse_code_letters,start=97)}
        
        res = set()
        
        for word in words:
            current_word_in_morse = ''
            for letter in word:
                current_word_in_morse += morse_to_alpha[letter]
            res.add(current_word_in_morse)
        return len(res)
        
        
