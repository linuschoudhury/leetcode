class Solution(object):
    def longestPalindrome(self, s):
        count = {}
        for char in s:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
        even = 0
        hasOdd=0
        for value in count.values():
            even = even+value//2*2
            if value%2==1:
                hasOdd = 1
        return even+hasOdd