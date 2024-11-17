class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars=list(s)
        n=len(chars)
        left=0
        right=n-1
        while left<right:
            if chars[left].isalpha()==False:
                left+=1
            if chars[right].isalpha()==False:
                right-=1
            if chars[left].isalpha() and chars[right].isalpha():
                chars[left],chars[right]=chars[right],chars[left]
                left+=1
                right-=1
        return ''.join(chars)
        