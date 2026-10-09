class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ConcatList = list(nums) + list(nums)
        return ConcatList