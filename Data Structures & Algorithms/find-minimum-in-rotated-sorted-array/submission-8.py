class Solution:
    def findMin(self, nums: List[int]) -> int:
        MinNum = nums[0]
        for i in range(len(nums)):
            if nums[i] < MinNum:
                MinNum = nums[i]
        return MinNum


