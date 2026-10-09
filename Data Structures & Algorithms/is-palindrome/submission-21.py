class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalnum())
        l = 0
        r = len(s) - 1
        while r > l:
            if s[r] == s[l]:
                l += 1
                r -= 1
            else:
                return False
        return True