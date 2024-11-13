class Solution(object):
    def mergeAlternately(self, word1, word2):
        left,right=0,0
        word3=[]
        while left<len(word1) and right<len(word2):
            word3.append(word1[left])
            word3.append(word2[right])
            left+=1
            right+=1
        while left<len(word1):
            word3.append(word1[left])
            left+=1
        while right<len(word2):
            word3.append(word2[right])
            right+=1
        return ''.join(word3)
        

        