class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice=prices[0]
        maxprofit=[0]*len(prices)
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            maxprofit[i]=prices[i]-minprice
        print maxprofit
        return max(maxprofit)
        