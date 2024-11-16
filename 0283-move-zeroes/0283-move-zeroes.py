class Solution(object):
    def moveZeroes(self, nums):
        left=0
        right=0
        while left<len(nums):
            if nums[left]!=0:
                if nums[right]==0:
                    nums[left],nums[right]=nums[right],nums[left]
                right+=1
            left+=1
                
            

        
        


        