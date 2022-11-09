class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        
        d = dict()
        for i in range(len(s)):
            cur_letter = s[i]
            if cur_letter in d:
                d[cur_letter] = (i - d[cur_letter]) - 1
                position = ord(cur_letter) - 97
                possible_distance = distance[position]
                if possible_distance != d[cur_letter]:
                    return False
                
            else:
                d[cur_letter] = i
        return True
