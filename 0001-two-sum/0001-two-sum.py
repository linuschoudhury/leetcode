class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        find=0
        for i,num in enumerate(nums):
            find = target-num
            if find in hashmap:
                return i,hashmap[find]
            hashmap[num]=i
        return False