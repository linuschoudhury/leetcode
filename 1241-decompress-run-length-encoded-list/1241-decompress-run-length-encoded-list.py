class Solution(object):
    def decompressRLElist(self, nums):
        result=[]
        for i in range(len(nums)):
            if i%2==0:
                result.extend([nums[i+1]]*nums[i])
        return result
        