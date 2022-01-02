
'''Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].'''

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        zipped =  [*zip(nums[:n], nums[n:])]

        result = []
        for i,k in zipped:
            result.append(i)
            result.append(k)
        return result1470. Shuffle the Array
