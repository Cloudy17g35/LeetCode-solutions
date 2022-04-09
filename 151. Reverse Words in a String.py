class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = re.sub(' +', ' ', s)
        s = s.strip()
        s = s.split()[::-1]
        
        return ' '.join(s)
