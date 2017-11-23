#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 518_Coin_Change_2.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #第一思路，DP
    #dp[i]存储amout为i时的可能结果
    #对于每种硬币，都把它变为很多种硬币比如2变为2,4,6,8分别表示不同个数。防止出现重复
    #TLE。分析：
    #子问题重复了，因为从+2，+4，+6,+8需要计算4n次，而其实只需要计算n次，即+2算出+2的中间结果，+4是从+2算过去的。+6是从+4算过去的。
    def change(self, amount, coins):
        dp = [1] + [0] * amount
        for coin in coins:
            start = coin
            newdp = dp[:]
            while start <= amount:
                for i in range(amount - start + 1):
                    newdp[i + start] += dp[i]
                start += coin
            dp = newdp
        return dp[-1]

    #O(mn)DP
    #dp[i][j]表示使用前i种coin来组成j的可能性。
    #本质跟上面思路一样,不断增加新一种的硬币，计算结果。
    def change2(self, amount, coins):
        if not coins: return 1 if amount == 0 else 0
        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1
            for j in range(1, amount + 1):
                dp[i][j] = dp[i-1][j] + (dp[i][j-coins[i - 1]] if j >= coins[i - 1] else 0)
        return dp[-1][-1]


    #优化空间复杂度
    def change3(self, amount, coins):
        if not coins: return 1 if amount == 0 else 0
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]




amount = 5
coins = [1, 2, 5]
solute = Solution()
res = solute.change3(amount, coins)