class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join(i.lower() for i in s if i.isalnum())
        a = 0
        b = len(new_s) - 1
        while a < b:
            if new_s[a] != new_s[b]:
                return False
            a += 1
            b -= 1
        return True