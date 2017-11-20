#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-14
#difficulty degree：
#problem: 122_Best_Time_to_Buy_and_Sell_Stock_II
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #如果当前价格比买的贵，那就卖
    def maxProfit(self, prices):
        if not prices:
            return 0
        buy_price = prices[0]
        res = 0
        for j in range(1, len(prices)):
            #当今天的价格大于买入的价格，那么卖出股票，并买入今天的股票
            if prices[j] > buy_price:
                res += prices[j] - buy_price
                buy_price = prices[j]
            #若今天的价格小于买入的价格，那么不买那个股票，买今天的股票
            else:
                buy_price = prices[j]
        return res


    def maxProfit(self, prices):
        if not prices: return 0
        l = len(prices)
        dp_buy = -prices[0]
        dp_sell = 0
        for i in range(1, l):
            dp_sell, dp_buy = max(dp_sell, dp_buy + prices[i]), max(dp_sell - prices[i], dp_buy)
        return max(dp_buy, dp_sell)




prices = [1,4,2]
solute = Solution()
res = solute.maxProfit(prices)
print(res)