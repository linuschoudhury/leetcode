class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars=list(s)
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        i=0
        j=len(chars)-1
        while i<=j:
            if chars[i] not in vowels and chars[j] not in vowels:
                i+=1
                j-=1
            elif chars[i] in vowels and chars[j] not in vowels:
                j-=1
            elif chars[i] not in vowels and chars[j] in vowels:
                i+=1
            else:
                chars[i],chars[j]=chars[j],chars[i]
                i+=1
                j-=1
        return ''.join(chars)
        