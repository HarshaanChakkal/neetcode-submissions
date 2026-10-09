class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1'''
        l = 0
        r = len(nums) - 1
        while r >= l:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m

        return -1