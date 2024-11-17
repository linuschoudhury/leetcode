class Solution(object):
    def intersection(self, nums1, nums2):
        hash=set()
        if len(nums1)>len(nums2):
            for num in nums1:
                if num in nums2:
                    hash.add(num)
        else:
            for num in nums2:
                if num in nums1:
                    hash.add(num)
        return list(hash)

        