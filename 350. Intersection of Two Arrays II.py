'''Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = Counter(nums1)
        d2 = Counter(nums2)

        inter = d1 & d2

        result = []

        for key, value in inter.items():
            for _ in range(value):
                result.append(key)

        return result
