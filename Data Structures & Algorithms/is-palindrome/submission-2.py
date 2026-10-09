class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        c1 = 0
        c2 = len(s) - 1
        while c1 < c2:
            if s[c1] != s[c2]:
                return False
            c1 += 1
            c2 -= 1
        return True

            