class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        goodpair = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j] and j>i:
                    goodpair+=1
        return goodpair
        