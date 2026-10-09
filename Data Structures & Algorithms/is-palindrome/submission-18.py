class Solution:
    def isPalindrome(self, s: str) -> bool:
        joinedS = ''.join(i.lower() for i in s if i.isalnum())
        l = 0
        r = len(joinedS) - 1
        while r > l:
            if joinedS[l] == joinedS[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
