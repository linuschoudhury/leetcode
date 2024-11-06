class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashmap = {}
        for i,num in enumerate(nums):
            if num in hashmap and i-hashmap[num]<=k:
                return True
            hashmap[num]=i
        return False
        