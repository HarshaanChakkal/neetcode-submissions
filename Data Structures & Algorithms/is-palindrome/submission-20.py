class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i.lower() for i in s if i.isalnum())
        l = 0
        r = len(s) - 1
        while r > l:
            if s[l] == s[r]:
                r -= 1
                l += 1
            else:
                return False
        return True