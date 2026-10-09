class Solution:
    def isPalindrome(self, s: str) -> bool:
        sorted_s = ''.join(i.lower() for i in s if i.isalnum())
        l = 0
        r = len(sorted_s) - 1
        while r > l:
            if sorted_s[l] == sorted_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
                
                