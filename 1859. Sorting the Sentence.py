class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        
        numbers = set(list(range(1, len(s) + 1)))
        
        for word in s.split():
            for number in numbers :
                if str(number) in word:
                    d[number] = word.replace(str(number), '')
                    
        print(d)
        return ' '.join(([d[key] for key in sorted(d.keys())]))
