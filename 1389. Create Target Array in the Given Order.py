class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            current_num = nums[i]
            current_index = index[i]
            target.insert(current_index,current_num)
        return target[:len(nums)]
