class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(score, reverse=True)
        ranks = {score: str(i) for i, score in enumerate(sorted_scores, start=1)}
        medals_mapper = {'1': "Gold Medal",
                        '2' : "Silver Medal",
                        '3' : "Bronze Medal"}
        res = []
        for s in score:
            cur_placement = ranks[s]
            if cur_placement in medals_mapper:
                cur_placement = medals_mapper[cur_placement]
            res.append(cur_placement)
        return res
