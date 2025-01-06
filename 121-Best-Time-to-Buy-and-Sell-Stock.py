class Solution(object):
    def maxProfit(self, prices):
        \\\
        :type prices: List[int]
        :rtype: int
        \\\
        profit = 0
        L = 0
        for R in range(len(prices)):
            if prices[R] < prices[L]:
                L=R
            profit = max(profit, prices[R]-prices[L])
        
        return 0 if profit<0 else profit