#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 309_Best_Time_to_Buy_and_Sell_Stock_with_Cooldown
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #使用三个数组代表到当前price时，最后一次操作为买，卖，休息的最大收益
    def maxProfit(self, prices):
        l = len(prices)
        if l < 2: return 0
        buy, sell, rest = [0] * l, [0] * l, [0] * l
        buy[0] = -prices[0]
        for i in range(1, l):
            buy[i] = max(buy[i - 1], rest[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            rest[i] = sell[i - 1]
        return sell[-1]

    #优化空间复杂度
    def maxProfit(self, prices):
        l = len(prices)
        if l < 2: return 0
        buy, sell, prebuy, presell = -prices[0], 0, 0, 0
        for i in range(1, l):
            prebuy = buy
            buy = max(prebuy, presell - prices[i])
            presell = sell
            sell = max(presell, prebuy + prices[i])
        return sell

