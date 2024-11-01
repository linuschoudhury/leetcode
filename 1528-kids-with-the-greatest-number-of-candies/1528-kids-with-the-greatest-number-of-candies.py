class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        largest = 0
        result = [0]*len(candies)
        for candy in candies:
            if candy>largest:
                largest = candy
        for i in range(len(candies)):
            if extraCandies+candies[i]>=largest:
                result[i]=True
            else:
                result[i]=False
        return result
        