class Solution(object):
    def lengthOfLastWord(self, s):
        s=s[::-1]
        count = 0
        started = False
        for char in s:
            if char.isspace():
                if started:
                    return count
            if char.isalnum():
                started=True
                count+=1
        return count
                
                
        
            
        