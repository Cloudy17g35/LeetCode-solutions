class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        
        distances = [[releaseTimes[0], keysPressed[0]]]
        
        for i in range(len(releaseTimes) - 1):
            release_time = releaseTimes[i + 1] - releaseTimes[i]
            button_index = i + 1
            letter = keysPressed[button_index]
            distances.append([release_time, letter])
        return sorted(distances, reverse=True)[0][1]
