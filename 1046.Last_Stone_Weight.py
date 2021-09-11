class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1 and stones[0] != 0:
            stones.sort(reverse=True)
            if stones[0] - stones[1] > 0:
                stones.append(stones[0] - stones[1])
                del stones[0]
                del stones[0]
            elif stones[0] == stones[1]:
                del stones[0], stones[0]
        return stones[0] if stones else 0
