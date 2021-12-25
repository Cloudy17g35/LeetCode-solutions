'''A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.'''


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        maximal_length = 0
        
        for sentence in sentences:
            sentence = sentence.split()
            length_of_sentence = len(sentence)
            
            if length_of_sentence > maximal_length:
                maximal_length = length_of_sentence
                
        return maximal_length
