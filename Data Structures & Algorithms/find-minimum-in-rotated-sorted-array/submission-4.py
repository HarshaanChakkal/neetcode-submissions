class Solution:
    def findMin(self, nums: List[int]) -> int:
        #return min(nums)
        #[3, 4, 5, 6, 1, 2] 5 > 2
        l = 0
        r = len(nums) - 1
        while r > l:
            m = (r + l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]