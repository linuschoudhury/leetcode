class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        s=''.join(char for char in s if char.isalnum())
        if s==s[::-1]:
            return True
        return False
        