class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l, r = 0, len(heights) - 1
        while r > l:
            height = min(heights[l], heights[r])
            width = r - l
            res = max(res, height * width)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return res