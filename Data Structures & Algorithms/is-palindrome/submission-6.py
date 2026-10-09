class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalnum())
        s1 = 0
        s2 = len(s) - 1
        if len(s) <= 1:
            return True
        while s1 < s2:
            if s[s1] != s[s2]:
                return False
            s1 += 1
            s2 -= 1
        return True