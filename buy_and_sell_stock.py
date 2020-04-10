"""
Say you have an array prices for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like
(i.e., buy one and sell one share of the stock multiple times).
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for i in range(len(prices)-1):
            if(0 < prices[i+1]- prices[i] <= max(prices)):
                total_profit += prices[i+1]- prices[i]
        return total_profit
