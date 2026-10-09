class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_s = ''.join(i.lower() for i in s if i.isalnum())
        a = 0
        b = len(sorted_s) - 1
        while b > a:
            if sorted_s[a] != sorted_s[b]:
                return False
            else:
                a += 1
                b -= 1
        return True