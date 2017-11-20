#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-4-
#difficulty degree：
#problem: 121_best_time_to_sell_and_buy_stock
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        res = 0
        for price in prices:
            min_price = min(min_price, price)
            res = max(res, price - min_price)
        return res


prices = [7,1,5,3,6,4]
solute = Solution()
res = solute.maxProfit(prices)
print(res)