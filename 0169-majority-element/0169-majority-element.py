class Solution(object):
    def majorityElement(self, nums):
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        return max(count, key=count.get)

            