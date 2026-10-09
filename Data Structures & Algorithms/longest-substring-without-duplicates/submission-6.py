class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in set_s:
                set_s.remove(s[l])
                l += 1
            set_s.add(s[r])
            res = max(res, r - l + 1)
        return res