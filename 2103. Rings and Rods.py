''' DESCRIPTION:  https://leetcode.com/problems/rings-and-rods/'''

class Solution:
    def countPoints(self, rings: str) -> int:
        k = 2
        d = {}
        count = 0

        for i in range(0, len(rings), 2):
            ring = rings[i:k]
            k += 2
            color, number = ring[0], ring[1]
            if number not in d:
                d[number] = set(color)
            else:
                d[number].add(color)

        for key in d:
            if d[key] == {'G', 'R', 'B'}:
                count += 1
        
        return count
