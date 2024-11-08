class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buyprice=prices[0]
        maxprofit=[0]*len(prices)
        for i in range(len(prices)):
            if prices[i]<buyprice:
                buyprice=prices[i]
            maxprofit[i]=prices[i]-buyprice
        return max(maxprofit)
        