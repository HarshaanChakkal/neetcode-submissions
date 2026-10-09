class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l = 0
        s, t = sorted(s), sorted(t)
        while l < len(s):
            if s[l] == t[l]:
                l += 1
            else:
                return False
        return True