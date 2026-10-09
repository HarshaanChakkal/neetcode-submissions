class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        charSet = set(s)
        for i in charSet:
            count = l = 0
            for j in range(len(s)):
                if s[j] == i:
                    count += 1
                while (j - l + 1) - count > k:
                    if s[l] == i:
                        count -= 1
                    l += 1
                res = max(res, j - l + 1)
        return res