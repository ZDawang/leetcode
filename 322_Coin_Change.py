#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-7-4
#difficulty degree：
#problem: 322_Coin_Change
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #dp
    def coinChange(self, coins, amount):
        d = {0: 0}
        l = len(coins)
        for i in range(1, amount + 1):
            mincoin = amount
            index = 0
            for j in range(l):
                if i - coins[j] in d:
                    index = 1
                    mincoin = min(d[i - coins[j]] + 1, mincoin)
            if index:
                d[i] = mincoin
        return d.get(amount, -1)

    #dp，优化，dp存储到当前的最小硬币数
    def coinChange2(self, coins, amount):
        dp = [0] + [0]*amount
        for i in range(1, amount + 1):
            mincoin = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    mincoin = min(mincoin, dp[i - coin] + 1)
            dp[i] = mincoin
        return dp[amount] if dp[amount] != amount + 1 else -1

    #BFS
    def coinChange2(self, coins, amount):
        visited, visiting = {0}, {0}
        count = 0
        while(visiting):
            visiting = {a + c for a in visiting for c in coins if a + c <= amount} - visited
            visited = visiting | visited
            count += 1
            if amount in visiting:
                return count
        return -1 if amount != 0 else 0




coins = [186,419,83,408]
solute = Solution()
res = solute.coinChange(coins, 6249)
print(res)