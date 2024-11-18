class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count=0
        left=0
        right=len(nums)-1
        nums.sort()
        for i in range(len(nums)):
            if nums[left]+nums[right]>=target:
                right-=1
            else:
                count+=right-left
                left+=1
        return count
        