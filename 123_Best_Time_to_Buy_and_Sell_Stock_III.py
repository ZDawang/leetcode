#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-5-14
#difficulty degree：
#problem: 123_Best_Time_to_Buy_and_Sell_Stock_III
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #正向寻找最大值，反向寻找最大值
    #正向的i为卖出，反向的i为购买。所以两个加一起就为结果。
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        pos_max_price = 0
        pos_prices = [0 for i in range(len(prices))]
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            pos_max_price = max(pos_max_price, prices[i] - min_price)
            pos_prices[i] = pos_max_price

        max_price = prices[-1]
        opp_max_price = 0
        opp_prices = [0 for i in range(len(prices))]
        for i in range(len(prices) - 1, 0, -1):
            max_price = max(prices[i], max_price)
            opp_max_price = max(opp_max_price, max_price - prices[i])
            opp_prices[i] = opp_max_price

        res = 0
        for i in range(len(prices)):
            res = max(res, opp_prices[i] + pos_prices[i])
        return res



prices = [2,1,2,0,1]
solute = Solution()
res = solute.maxProfit(prices)
print(res)