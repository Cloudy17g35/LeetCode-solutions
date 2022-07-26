class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key = key.replace(' ', '')
        unique_letters = []
        for l in key:
            if l not in unique_letters:
                unique_letters.append(l)
        alpha_letters = [chr(97 + i) for i in range(len(unique_letters))]
        decode_map = dict(zip(unique_letters, alpha_letters))
        
        decoded_message = ''
        
        for l in message:
            if l == ' ':
                decoded_message += ' '
            else:
                decoded_message += decode_map[l]
        return decoded_message
        
