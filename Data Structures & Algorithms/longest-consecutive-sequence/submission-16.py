class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        count = 0
        for i in nums:
            if i - 1 not in nums:
                length = 1
                while i+length in nums:
                    length += 1
                count = max(count, length)
        return count