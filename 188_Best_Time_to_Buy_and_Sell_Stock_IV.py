#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 188_Best_Time_to_Buy_and_Sell_Stock_IV.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp
    #使用dp[i][j]来代表到i为止，进行了j次交易的最大利润
    #使用dp[i][j] = max(dp[i-1][j], max(dp[i-h][j-1] + prices[i] - prices[h]) for h in range(i))来进行更新
    #也就是dp[i][j] = max(dp[i-1][j], prices[i] + max(dp[i-h][j-1] - prices[h]) for h in range(i)))
    #所以可使用buy来存储max(dp[i-h][j-1] - prices[h]) for h in range(i)，也就是进行j-1次交易后，把j次的股票先买了以后的最大利润
    #所以buy[i][j] = max(buy[i-1][j], dp[i][j] - prices[i])

    #O(kn) TLE.......
    #加入122题的情况，当k>=l//2时，说明可以任意买卖。
    #是l//2的原因是 如果是[1,2,3,4]这种情况，可以一次买卖就行了。只有[1,2,1,2]这种情况需要2次买卖，所以最多只需要进行l//2次买卖
    def maxProfit(self, k, prices):
        l = len(prices)
        if l < 2: return 0
        if k >= l//2:
            return self.maxProfit_nolimit(prices)
        dp = [0 for _ in range(k + 1)]
        buy = [-prices[0] for _ in range(k + 1)]
        for i in range(1, l):
            price = prices[i]
            for j in range(1, k + 1):
                dp[j] = max(dp[j], price + buy[j - 1])
                buy[j - 1] = max(buy[j - 1], dp[j - 1] - price)
        return dp[-1]

    def maxProfit_nolimit(self, prices):
        if not prices: return 0
        dp_buy = -prices[0]
        dp_sell = 0
        for i in range(1, len(prices)):
            dp_sell, dp_buy = max(dp_sell, dp_buy + prices[i]), max(dp_sell - prices[i], dp_buy)
        return max(dp_buy, dp_sell)

k = 3
prices = [8,7,6,5,4,3,2,1,3]
solute = Solution()
res = solute.maxProfit(k, prices)