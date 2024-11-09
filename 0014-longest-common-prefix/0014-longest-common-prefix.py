class Solution(object):
    def longestCommonPrefix(self, strs):
        lengths=[]
        res=''
        for i in range(len(strs)):
            lengths.append(len(strs[i]))
        minlength = min(lengths)
        for i in range(minlength):
            for s in strs:
                if s[i]!=strs[0][i]:
                    return res
            res+=strs[0][i]
        return res
            
            
        