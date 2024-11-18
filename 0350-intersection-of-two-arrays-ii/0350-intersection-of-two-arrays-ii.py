class Solution(object):
    def intersect(self, nums1, nums2):
        hash = {}
        result=[]
        for num in nums1:
            if num in hash:
                hash[num]+=1
            else:
                hash[num]=1
        for num in nums2:
            if num in hash and hash[num]>0:
                result.append(num)
                hash[num]-=1
        print(hash)
        #for key, value in hash.items():
            #result.extend([key] * value)
        return result
        
        