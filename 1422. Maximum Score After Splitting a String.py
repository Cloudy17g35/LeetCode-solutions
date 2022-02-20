class Solution:
    def maxScore(self, s: str) -> int:

        maximal_sum = 0

        for i in range(len(s) - 1):
            first_part, second_part = s[:i + 1], s[i + 1:]

            score_first, score_second = first_part.count('0'), second_part.count('1')

            current_max = score_first + score_second

            if current_max > maximal_sum:
                maximal_sum = current_max

        return maximal_sum
