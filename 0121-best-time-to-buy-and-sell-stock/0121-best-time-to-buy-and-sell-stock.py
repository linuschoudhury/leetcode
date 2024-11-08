class Solution(object):
    def maxProfit(self, prices):
        buyprice=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<buyprice:
                buyprice=prices[i]
            maxprofit=max(prices[i]-buyprice,maxprofit)
        return maxprofit
        