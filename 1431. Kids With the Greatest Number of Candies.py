'''https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/'''

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        all_candies = [candy + extraCandies for candy in candies]

        maximal_amount = max(candies)

        return [candy >= maximal_amount for candy in all_candies]
