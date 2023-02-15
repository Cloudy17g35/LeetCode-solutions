class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k:
            maximal_value = max(gifts)
            for i in range(len(gifts)):
                if gifts[i] == maximal_value:
                    gifts[i] = int(math.sqrt(gifts[i]))
                    break
            k -= 1
        return sum(gifts)
