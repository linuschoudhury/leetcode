class Solution(object):
    def twoSum(self, numbers, target):
        hashmap = {}
        find=0
        for i,num in enumerate(numbers):
            find = target-num
            if find in hashmap:
                return hashmap[find]+1, i+1
            hashmap[num]=i
        