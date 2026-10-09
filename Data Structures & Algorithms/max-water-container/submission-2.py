class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # [1, 4, 7, 3, 5, 6, 9, 1]
        l = 0
        r = len(heights) - 1
        res = 0
        while r > l:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
        return res
