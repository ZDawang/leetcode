#!/usr/bin/python
# -*- coding: utf-8 -*-

#author : zhangdawang
#data: 2017-10
#difficulty degree：
#problem: 174_Dungeon_Game.py
#time_complecity:  
#space_complecity: 
#beats: 

class Solution(object):
    #从右下向左上遍历，因为终点的血量肯定是1.
    def calculateMinimumHP(self, dungeon):
        if not dungeon or not dungeon[0]: return 0
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]
        #因为到公主这里之后，需要剩余1的血量
        dp[m][n - 1], dp[m - 1][n] = 1, 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                #根据后面需要的血量计算当前位置向后需要的血量。
                #若当前位置需要的血量超过1，前面需要多少血量，仍然是需要多少血量。所以max(XX, 1)
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]







dungeon = [[1,-2,3],[2,-2,-2]]
solute = Solution()
res = solute.calculateMinimumHP(dungeon)
